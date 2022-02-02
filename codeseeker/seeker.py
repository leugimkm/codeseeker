import requests  # type: ignore
from typing import Dict, List, Optional, Union
import webbrowser

from validators import (
    validate_response, validate_data_links, validate_keyword
)


class Query:
    """Representation of a query.

    Attributes:
        github (str): GitHub url.
        base (str): The base url.
        repo (str): The name of the repository.
        lang (str): Target Programming language of the keyword.
        query (str): Query that performs the search.
        url (str): The url to be used by requests.
        link (str): Github link to the file.
        tag (str): The tag used in the response.
    """

    def __init__(self) -> None:
        self._set_defaults()

    def _set_defaults(self):
        self.github = "https://github.com/"
        self.base = "https://api.github.com/search/code"
        self.repo = "AyudaEnPython/Soluciones"
        self.lang = "python"
        self.query = "?q={}+in%3afile+language%3a{}+repo%3a{}"
        self.url = self.base + self.query
        self.link = self.github + "{}/blob/main/{}"
        self.tag = "path"


class Seeker:
    """Seeker that searchs for code on GitHub.

    Attributes:
        q (Query): Query object.
    """

    def __init__(self) -> None:
        self.q = Query()

    def search(
        self,
        keyword: str,
        repo: Optional[str] = None,
        lang: Optional[str] = None,
        tag: str = "items",
    ) -> Union[List[Dict[str, str]], None]:
        """Search for a keyword in a GitHub repository.

        Args:
            keyword (str): Keyword to search.
            repo (str, optional): Repository to search.
            lang (str, optional): Programming language target.
            tag (str, optional): Tag to be used to search. Defaults
                to "items".

        Raises:
            SearchException: If the response is not 200.
            ValidationException: If the keyword is not valid.

        Returns:
            Union[List[Dict[str, str]], None]: The data.
        """
        if repo is not None:
            self.q.repo = repo
        if lang is not None:
            self.q.lang = lang
        try:
            validate_keyword(keyword)
        except Exception as e:
            print(e)
            return None
        url = self.q.url.format(keyword, self.q.lang, self.q.repo)
        response = requests.get(url)
        try:
            validate_response(response)
            return response.json()[tag]
        except Exception as e:
            print(e)
            return None


def open_url(
    seeker: Seeker,
    data: List[Dict[str, str]],
) -> None:
    """Open the results in a web browser.

    Args:
        seeker (Seeker): Seeker object.
        data (List[Dict[str, str]]: Data received from the search.
        tag (str, optional): Tag that will be used to open the URL.
    
    Raises:
        ValidationException: If the data is empty.
    """
    try:
        validate_data_links(data)
        print("\nOpening in a web browser...")
        for link in data:
            webbrowser.open_new_tab(
                seeker.q.link.format(seeker.q.repo, link[seeker.q.tag])
            )
    except Exception as e:
        print(e)


def to_txt(
    seeker: Seeker,
    data: List[Dict[str, str]],
) -> None:
    """Saves the results in a text file.
    
    Args:
        seeker (Seeker): Seeker object.
        data (List[Dict[str, str]]: Data received from the search.

    Raises:
        ValidationException: If the data is empty.
    """
    try:
        validate_data_links(data)
        print("\nSaving in a text file...")
        with open("results.txt", "w") as f:
            for link in data:
                f.write(seeker.q.link.format(
                    seeker.q.repo, link[seeker.q.tag])
                )
                f.write("\n")
    except Exception as e:
        print(e)
