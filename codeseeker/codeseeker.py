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
    ...


def display_data(data: List[str], tag: str = "path") -> None:
    ...


def main():
    parser = argparse.ArgumentParser(
        prog="codeseeker",
        description="Search code through a GitHub repository.",
        epilog="",
    )


if __name__ == "__main__":
    main()