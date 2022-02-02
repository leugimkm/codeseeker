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

For more information, see:
https://leugimkm.github.io/codeseeker/
"""
from .base import parse_args
from .seeker import Seeker, open_url, to_txt
from .utils import show


def main():
    args = parse_args()
    seeker = Seeker()

    if args.repo:
        seeker.repo = args.repo
    if args.lang:
        seeker.lang = args.lang
    if args.tag:
        seeker.tag = args.tag

    data = seeker.search(args.keyword, args.repo, args.lang)

    if data is None:
        print("No results found.")
    else:
        if args.keyword:
            show(data)
        if args.open:
            open_url(seeker, data)
        if args.txt:
            to_txt(seeker, data)


if __name__ == "__main__":
    main()
