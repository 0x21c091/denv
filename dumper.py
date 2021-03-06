from collections import OrderedDict
from os import environ
from types import NoneType
from typing import Dict, Mapping, List, Optional, Set

Store = Mapping[str, str]


def _parse(file: str) -> Store:
    parsed = {}

    with open(file) as env_file:
        for line in env_file:
            line = line.strip()

            if not line or line.startswith('#') or '=' not in line:
                continue

            name, value = line.split('=', 1)
            name = name.strip()
            value = value.strip()
            parsed[name] = value

    return parsed


def _env_os(keys: Set[str]) -> Store:
    env_os = {}

    for name, value in environ.items():
        if keys and name not in keys:
            continue
        env_os[name] = value

    return env_os


def dump(files: List[str], env_os: Optional[bool] = False, env_os_strict: Optional[bool] = False) -> Dict[str, str]:
    store: Dict[str, str] = {}

    if files:
        for file in files:
            store.update(_parse(file))

    if env_os:
        keys = {}
        if env_os_strict:
            keys = store.keys()
        store.update(_env_os(keys))

    return OrderedDict(sorted(store.items()))
