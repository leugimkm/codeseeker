import configparser
import requests  # type: ignore
from typing import Dict, List
import webbrowser

from validators import validate_response, validate_data_links


class Query:
    """Representation of a query.

    Attributes:
        config (str, object): The configuration object.
        github (str): GitHub url.
        base (str): The base url.
        repo (str): The name of the repository.
        lang (str): Target Programming language of the keyword.
        query (str): Query that performs the search.
        url (str): The url to be used by requests.
        link (str): Github link to the file.
    """

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self._set_defaults()

    def _set_defaults(self):
        self.github = self.config["DEFAULT"]["github_url"]
        self.base = self.config["DEFAULT"]["base_url"]
        self.repo = self.config["DEFAULT"]["repo"]
        self.lang = self.config["DEFAULT"]["language"]
        self.query = "?q={}+in%3afile+language%3a{}+repo%3a{}"
        self.url = self.base + self.query
        self.link = self.github + "{}/blob/main/{}"


class Seeker:
    """Seeker that searchs for code on GitHub.

    Attributes:
        q (Query): The query object.
    """

    def __init__(self) -> None:
        self.q = Query()

    def search(
        self,
        keyword: str,
        tag: str = "items"
    ) -> List[Dict[str, str]]:
        """Search for a keyword in a GitHub repository.

        Args:
            keyword (str): The keyword to search.

        Raises:
            SearchException: If the response is not 200.

        Returns:
            List[dict]: The search results.
        """
        response = requests.get(self.q.url.format(
            keyword,
            self.q.lang,
            self.q.repo,
        ))
        try:
            validate_response(response)
            return response.json()[tag]
        except Exception as e:
            print(e)
        return []


def open_url(
    seeker: Seeker,
    data: List[Dict[str, str]],
    tag: str = "path",
) -> None:
    """Open the URL.

    Args:
        seeker (Seeker): The Seeker object.
        data (List[Dict[str, str]]: Data that will be used to open the
            URL.
        tag (str, optional): Tag that will be used to open the URL.
    """
    try:
        validate_data_links(data)
        print("\nOpening in a web browser...")
        for link in data:
            webbrowser.open_new_tab(
                seeker.q.link.format(seeker.q.repo, link[tag])
            )
    except Exception as e:
        print(e)
