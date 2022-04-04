from setuptools import setup

setup(
    name='ts-spdx-import',

    packages=['ts_spdx_import'],

    version='1.0.0',

    description='An SPDX importer for TrustSource (https://app.trustsource.io) to manage open source code compliance',

    author='EACG GmbH',

    license='ASL-2.0',

    url='https://github.com/TrustSource/ts-spdx-upload.git',

    download_url='',

    keywords=['scanning', 'dependencies', 'modules', 'TrustSource'],

    classifiers=[],

    install_requires=[
        'requests',
        'click',
        'packageurl-python',
        'license-expression',
        'ts-python-client==1.1.0',
        'spdx-tools @ git+https://github.com/TrustSource/tools-python.git@dev#egg=spdx-tools',
    ],

    scripts=['ts-spdx-import'],

    entry_points={
        'console_scripts': ['ts-spdx-import=ts_spdx_import.cli:main'],
    },
)