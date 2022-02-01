#!/user/bin/env python
# -*- coding: utf-8 -*-

"""CodeSeeker

A simple tool to search for code on GitHub.

Usage example:
    > python -m codeseeker cube
    1 file(s) found(s).

    repository/path/to/file.py

    > python -m codeseeker cube -o
    1 file(s) found(s).

    repository/path/to/file.py

    Opening in a web browser...
"""
import argparse

from .seeker import Seeker, open_url
from .utils import show


def main():
    parser = argparse.ArgumentParser(
        prog="codeseeker",
        description=(
            "CodeSeeker is a simple tool to search for code on GitHub."
        ),
        epilog="",
    )
    parser.add_argument(
        "keyword",
        help="Keyword to be searched.",
    )
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="Open the results in a web browser.",
    )
    args = parser.parse_args()
    seeker = Seeker()
    data = seeker.search(args.keyword)
    if args.keyword:
        show(data)
    if args.open:
        open_url(seeker, data)


if __name__ == "__main__":
    main()
