import requests
from typing import List
import webbrowser

from validators import validate_response, validate_data_links


class Seeker:
    """Seeker that searches for a keyword in a file (source code) from a
    GitHub repository.
    
    Args:
        path (str, optional): The path to the config file.

    Attributes:
        github (str): GitHub url.
        base (str): The base url.
        repo (str): The name of the repository.
        lang (str): Target Programming language of the keyword.
        query (str): Query that performs the search.
        url (str): The url to be used by requests.
        link (str): Github link to the file.
    """
    
    def __init__(self, cfg: object) -> None:
        self.config = cfg
        self._set_defaults()
    
    def _set_defaults(self):
        self.github = self.config["DEFAULT"]["github_url"]
        self.base   = self.config["DEFAULT"]["base_url"]
        self.repo   = self.config["DEFAULT"]["repo"]
        self.lang   = self.config["DEFAULT"]["language"]
        self.query  = "{}+in%3afile+language%3a{}+repo%3a{}"
        self.url    = self.base + self.query
        self.link   = self.github + "{}/blob/main/{}"

    def search(self, keyword: str, tag: str = "items") -> List[dict]:
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
            self.lang,
            self.repo,
        ))
        try:
            validate_response(response)
            return response.json()[tag]
        except Exception as e:
            print(e)


def show(data: List[str], tag: str = "path") -> None:
    """Display the data.

    Args:
        data (List[str]): The data to be displayed.
    """
    for item in data:
        print(item[tag])
    print(f"\n{len(data)} file(s) found(s).")


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
        print("\nOpening in a web browser...")
        for link in data:
            webbrowser.open_new_tab(seeker.link.format(seeker.repo, link[tag]))
    except Exception as e:
        print(e)