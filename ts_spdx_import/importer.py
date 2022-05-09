from pathlib import Path
from typing import Optional
from packageurl import PackageURL
from spdx.package import Package
from license_expression import get_spdx_licensing

from ts_python_client import Scanner, Scan, License, Dependency
from .parser import parse

licensing = get_spdx_licensing()

class SPDXImporter(Scanner):
    def __init__(self):
        super().__init__()

    @property
    def is_folder_scanner(self):
        return False

    def run(self) -> Scan:
        return SPDXImporter.parse_doc(self.client.path)

    @staticmethod
    def parse_doc(path: Path) -> Scan:
        doc = parse(path)

        if not doc:
            raise ValueError('Cannot parse SPDX document')

        scan = Scan(doc.name, ns='spdx')

        for pkg in doc.packages:
            dep = SPDXImporter._create_dep(pkg)
            if dep:
                scan.dependencies.append(dep)

        return scan

    @staticmethod
    def _create_dep(pkg: Package,
                    use_purl_as_version = False,
                    parse_license_exprs = True) -> Optional[Dependency]:
        dep = None
        meta = {}

        pkg_mngr_info = None

        for ref in pkg.pkg_ext_refs:
            if ref.category == 'PACKAGE-MANAGER':
                pkg_mngr_info = ref

        if pkg_mngr_info and pkg_mngr_info.pkg_ext_ref_type == 'purl':
            try:
                purl = PackageURL.from_string(pkg_mngr_info.locator)
            except ValueError:
                purl = None

            if purl:
                key = SPDXImporter._map_purl_type(purl.type)
                if purl.namespace:
                    key += ':' + purl.namespace
                key += ':' + purl.name

                if not use_purl_as_version:
                    ver = pkg.version
                    meta['purl'] = pkg_mngr_info.locator
                else:
                    ver = pkg_mngr_info.locator

                dep = Dependency(key, pkg.name, versions=[ver])


        if dep and pkg.license_declared:
            lic_expr = pkg.license_declared.identifier
            if lic_expr not in ['NONE', 'NOASSERTION']:
                if parse_license_exprs:
                    parsed = licensing.parse(lic_expr)
                    symbols = parsed.symbols
                    dep.licenses = [License(str(s)) for s in symbols]
                else:
                    dep.licenses = [License(lic_expr)]


        if dep and meta:
            dep.meta = meta

        return dep


    @staticmethod
    def _map_purl_type(ty: str):
        # Aliasing
        if ty == 'maven':
            return 'mvn'
        else:
            return ty