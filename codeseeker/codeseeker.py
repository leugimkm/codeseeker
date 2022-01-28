import argparse
import configparser
import requests
from typing import List, Optional


class CodeSeekerException(Exception):
    """SearchException base class."""


def raise_exception(
    standart_msg: str,
    custom_msg: Optional[str] = None,
    ) -> CodeSeekerException:
    """Raise a CodeSeekerException.

    Args:
        standard_msg (str): Standard message.
        custom_msg (str, optional): Custom message.
    
    Raises:
        CodeSeekerException: An exception with a standard or custom message.
    """
    if custom_msg is None:
        raise CodeSeekerException(standart_msg)
    else:
        raise CodeSeekerException(custom_msg)


def validate_response(response: requests.Response) -> None:
    """Validate the response.

    Args:
        response (requests.Response): The response to be validated.

    Raises:
        CodeSeekerException: If the response status code is not 200.
    """
    if response.status_code != 200:
        raise raise_exception(f"Error: {response.status_code}")


class Seeker:
    
    def __init__(self, path: str = "codeseeker/config.ini") -> None:
        self.config = configparser.ConfigParser()
        self.config.read(path)
        self._set_defaults()
    
    def _set_defaults(self):
        """Set default values."""
        self.base_url = self.config["DEFAULT"]["base_url"]
        self.repo     = self.config["DEFAULT"]["repo"]
        self.language = self.config["DEFAULT"]["language"]
        self.query = "{}+in%3afile+language%3a{}+repo%3a{}"
        self.url = self.base_url + self.query

    def search(
        self,
        keyword: str,
        tag: str = "items",
    ) -> List[dict]:
        """Search for a keyword in a GitHub repository.

        Args:
            keyword (str): The keyword to search.

        Raises:
            SearchException: If the response is not 200.

        Returns:
            List[dict]: The search results.
        """
        response = requests.get(self.url.format(
            keyword,
            self.language,
            self.repo,
        ))
        validate_response(response)
        return response.json()[tag]


def display_data(data: List[str], tag: str = "path") -> None:
    """Display the data.

    Args:
        data (List[str]): The data to be displayed.
    """
    print(f"Found {len(data)} repositories.\n")
    for item in data:
        print(item[tag])


def main():
    parser = argparse.ArgumentParser(
        prog="codeseeker",
        description="Search code through a GitHub repository.",
        epilog="",
    )
    parser.add_argument(
        "keyword",
        help="Search for a keyword in the repository.",
    )
    args = parser.parse_args()
    seeker = Seeker()
    if args.keyword:
        data = seeker.search(args.keyword)
        display_data(data)


if __name__ == "__main__":
    main()