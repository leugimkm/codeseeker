#!/user/bin/env python
# -*- coding: utf-8 -*-

"""CodeSeeker

A simple tool to search a keyword in a file (source code) from a GitHub
repository.

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
import configparser

from seeker import Seeker, show, open_url


def main():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    parser = argparse.ArgumentParser(
        prog="codeseeker",
        description="Search code through a GitHub repository.",
        epilog="",
    )
    parser.add_argument(
        "keyword",
        help="Search for a keyword in the repository.",
    )
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="Open the results in the browser.",
    )
    args = parser.parse_args()
    seeker = Seeker(cfg)
    data = seeker.search(args.keyword)
    if args.keyword:
        show(data)
    if args.open:
        open_url(seeker, data)


if __name__ == "__main__":
    main()
