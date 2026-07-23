"""Command-line interface for the thefuck package."""

from __future__ import annotations

import argparse
import sys

from thefuck import __version__
from thefuck.core import greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="thefuck",
        description="A private practice package for MSDS610.",
    )
    parser.add_argument("name", nargs="?", default="world", help="name to greet")
    parser.add_argument("--version", action="version", version=f"thefuck {__version__}")
    args = parser.parse_args(argv)

    print(greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
