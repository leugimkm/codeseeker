from argparse import ArgumentParser


def parse_args():
    """Function to parse arguments."""
    parser = ArgumentParser(
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
    parser.add_argument(
        "-t",
        "--tag",
        action="store",
        help="Tag to be used to open the results.",
    )
    parser.add_argument(
        "--txt",
        action="store_true",
        help="Save the results in a text file.",
    )
    parser.add_argument(
        "-r",
        "--repo",
        action="store",
        help="Sets the repository to search.",
    )
    parser.add_argument(
        "-l",
        "--lang",
        action="store",
        help="Sets the language to search.",
    )
    parser.add_argument(
        "--links",
        action="store_true",
        help="Show the links of the results.",
    )
    return parser.parse_args()
