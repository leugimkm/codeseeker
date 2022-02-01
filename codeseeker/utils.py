from typing import List, Dict

WILDCARDS: str = ".,:;/\`'\"=*!?#$&+^|~<>()\{\}[]@"


def show(data: List[Dict[str, str]], tag: str = "path") -> None:
    """Display the data.

    Args:
        data (Dict[str, str]): The data to be displayed.
    """
    for item in data:
        print(item[tag])
    print(f"\n{len(data)} file(s) found(s).")