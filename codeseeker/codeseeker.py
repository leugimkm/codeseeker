import argparse
import configparser
from ctypes import Union
import requests
import webbrowser
from typing import List, Optional


class CodeSeekerException(Exception):
    """Base class for exceptions."""


class ValidationException(CodeSeekerException):
    """Exception raised when a validation function is called
    and the value is not valid.
    """


class NoLinkFoundException(CodeSeekerException):
    """Exception raised when no link is found."""


def _raise_validation_exception(
    standart_msg: str,
    custom_msg: Optional[str] = None,
    ) -> ValidationException:
    """Raise a ValidationException.

    Args:
        standard_msg (str): Standard message.
        custom_msg (str, optional): Custom message.
    
    Raises:
        ValidationException: An exception with a standard or custom message.
    """
    if custom_msg is None:
        raise ValidationException(str(standart_msg))
    else:
        raise ValidationException(str(custom_msg))


def validate_response(response: requests.Response) -> None:
    """Validate the response.

    Args:
        response (requests.Response): The response to be validated.

    Raises:
        CodeSeekerException: If the response status code is not 200.
    """
    if response.status_code != 200:
        raise ValidationException(f"Error: {response.status_code}")


def validate_data_links(data: List[str]) -> None:
    """Validate the data.

    Args:
        data (List[str]): The data to be validated.
    """
    if len(data) == 0:
        raise NoLinkFoundException(
            "Can't open in a webbrowser (there are no results)."
        )


class Seeker:
    
    def __init__(self, path: str = "codeseeker/config.ini") -> None:
        self.config = configparser.ConfigParser()
        self.config.read(path)
        self._set_defaults()
    
    def _set_defaults(self):
        """Set default values."""
        self.github_url = self.config["DEFAULT"]["github_url"]
        self.base_url = self.config["DEFAULT"]["base_url"]
        self.repo     = self.config["DEFAULT"]["repo"]
        self.language = self.config["DEFAULT"]["language"]
        self.query = "{}+in%3afile+language%3a{}+repo%3a{}"
        self.url = self.base_url + self.query
        self.link = self.github_url + "{}/blob/main/{}"

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
        try:
            validate_response(response)
            return response.json()[tag]
        except Exception as e:
            print(e)


def display_data(data: List[str], tag: str = "path") -> None:
    """Display the data.

    Args:
        data (List[str]): The data to be displayed.
    """
    
    for item in data:
        print(item[tag])
    print(f"\n{len(data)} repositories found.")


def open_url(
    seeker: Seeker,
    data: List[str],
    tag: str = "path",
) -> None:
    """Open the URL.

    Args:
        seeker (Seeker): The Seeker object.
        data (Union[str, List[str]]): Data that will be used to open the URL.
        tag (str, optional): Tag that will be used to open the URL.
    """
    try:
        validate_data_links(data)
        for link in data:
            webbrowser.open_new_tab(seeker.link.format(seeker.repo, link[tag]))
    except Exception as e:
        print(e)


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
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="Open the results in the browser.",
    )
    args = parser.parse_args()
    seeker = Seeker()
    data = seeker.search(args.keyword)
    if args.keyword:
        display_data(data)
    if args.open:
        open_url(seeker, data)


if __name__ == "__main__":
    main()