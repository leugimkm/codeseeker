from typing import List

WILDCARDS = ".,:;/\`'\"=*!?#$&+^|~<>()\{\}[]@"


def show(data: List[str], tag: str = "path") -> None:
    """Display the data.

    Args:
        data (List[str]): The data to be displayed.
    """
    for item in data:
        print(item[tag])
    print(f"\n{len(data)} file(s) found(s).")