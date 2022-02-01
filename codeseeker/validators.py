import requests # type: ignore
from typing import Dict, List, Optional


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


def validate_data_links(data: List[Dict[str, str]]) -> None:
    """Validate the data links.

    Args:
        data (List[str]): The data to be validated.
    """
    if len(data) == 0:
        raise NoLinkFoundException(
            "Can't open in a web browser (there are no results)."
        )