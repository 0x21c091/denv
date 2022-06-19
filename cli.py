import argparse
import sys
from typing import NoReturn

import dumper


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f',
        '--file',
        type=str,
        action='append',
        help='file to parse'
    )

    parser.add_argument(
        '-e',
        '--env-os',
        action='store_true'
    )

    parser.add_argument(
        '-es',
        '--env-os-strict',
        action='store_true'
    )

    return parser


def main() -> NoReturn:
    args = _create_parser().parse_args()

    dump_vars = dumper.dump(files=args.file, env_os=args.env_os, env_os_strict=args.env_os_strict)

    for name, value in dump_vars.items():
        sys.stdout.write(f'{name}={value}\n')
