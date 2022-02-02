import requests  # type: ignore
from typing import Dict, List, Optional

WILDCARDS: str = ".,:;/\`'\"=*!?#$&+^|~<>()\{\}[]@"  # noqa: W605


class CodeSeekerException(Exception):
    """Base class for exceptions."""


class ValidationException(CodeSeekerException):
    """Exception raised when a validation function is called and the
    value is not valid.
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
        ValidationException: An exception with a standard or custom
        message.
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
        ValidationException: If the response status code is not 200.
    """
    if response.status_code != 200:
        raise ValidationException(f"Error: {response.status_code}")


def validate_data_links(data: List[Dict[str, str]]) -> None:
    """Validate the data links.

    Args:
        data (List[str]): The data to be validated.

    Raises:
        NoLinkFoundException: If no link is found.
    """
    if len(data) == 0:
        raise NoLinkFoundException(
            "Can't open in a web browser (there are no results)."
        )


def validate_keyword(keyword: str) -> None:
    """Validate the keyword.

    Args:
        keyword (str): The keyword to be validated.

    Raises:
        ValidationException: If the keyword is not valid.
    """
    if len(keyword) == 0:
        _raise_validation_exception(
            "The keyword can't be empty.",
        )
    if len(keyword) > 100:
        _raise_validation_exception(
            "The keyword can't be longer than 100 characters.",
        )
    for char in keyword:
        if char in WILDCARDS:
            _raise_validation_exception(
                "The keyword can't contain wildcards.",
            )
