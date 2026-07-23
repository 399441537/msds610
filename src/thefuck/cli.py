"""Command-line interface for the thefuck package."""

from __future__ import annotations

import argparse
import sys

from thefuck import __version__, gotchas
from thefuck.core import greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="thefuck",
        description="A private practice package for MSDS610.",
    )
    parser.add_argument("--version", action="version", version=f"thefuck {__version__}")
    sub = parser.add_subparsers(dest="command")

    p_greet = sub.add_parser("greet", help="print a greeting")
    p_greet.add_argument("name", nargs="?", default="world", help="name to greet")

    p_gotchas = sub.add_parser("gotchas", help="list or explain common mistakes")
    p_gotchas.add_argument(
        "name", nargs="?", help="a gotcha name to explain (omit to list all)"
    )

    args = parser.parse_args(argv)

    if args.command == "gotchas":
        if args.name:
            print(gotchas.explain(args.name))
        else:
            print("Common gotchas (use `thefuck gotchas <name>` to explain):")
            for name in gotchas.list_gotchas():
                print(f"  - {name}: {gotchas.GOTCHAS[name].title}")
        return 0

    # default command is greet
    name = getattr(args, "name", "world") or "world"
    print(greet(name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
