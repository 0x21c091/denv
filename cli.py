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
        '--env',
        action='store_true'
    )

    return parser


def main() -> NoReturn:
    args = _create_parser().parse_args()

    dump_vars = dumper.dump(args.file, args.env)

    for name, value in dump_vars.items():
        sys.stdout.write(f'{name}={value}\n')
