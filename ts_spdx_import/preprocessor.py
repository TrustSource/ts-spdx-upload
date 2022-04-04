import json
from pathlib import Path


class Config:
    def __init__(self, ignored_fields: list[str] = None):
        self.ignored_fields = ignored_fields if ignored_fields else []


def preprocess(path: Path, cfg: Config) -> Path:
    if path.suffix in ['.json']:
        return __preprocess_json(path, cfg)

    return path


def __preprocess_json(path: Path, cfg: Config) -> Path:
    with path.open('r') as f:
        data = json.load(f)

    outpath = path.parent / (path.name + '_processed.json')
    with outpath.open('w') as f:
        json.dump(__filter(data, cfg), f)

    return outpath


def __filter(d, cfg: Config):
    if type(d) is dict:
        res = {}
        for k, v in d.items():
            if k not in cfg.ignored_fields:
                res[k] = __filter(v, cfg)

        return res

    elif type(d) is list:
        return  [__filter(v, cfg) for v in d]

    else:
        return d