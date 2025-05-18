# CodeSeeker

Search code through a GitHub repo.

![GitHub](https://img.shields.io/github/license/leugimkm/codeseeker)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](./code_of_conduct.md)
![GitHub languages](https://img.shields.io/github/languages/top/leugimkm/codeseeker)
![GitHub repo size](https://img.shields.io/github/repo-size/leugimkm/codeseeker)
![Github last-commit](https://img.shields.io/github/last-commit/leugimkm/codeseeker)
![maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/leugimkm/codeseeker)
![PyPI - Format](https://img.shields.io/pypi/format/codeseeker)
[![Downloads](https://pepy.tech/badge/codeseeker)](https://pepy.tech/project/codeseeker)

              .                 .
    ,-. ,-. ,-| ,-. ,-. ,-. ,-. | , ,-. ,-.
    |   | | | | |-' `-. |-' |-' |<  |-' |
    `-' `-' `-^ `-' `-' `-' `-' ' ` `-' '

`codeseeker` is simple tool to search for code on GitHub.
By default it searches to the contents of the source code file.

## Installation

`codeseeker` is available on [PyPi](https://pypi.org/project/codeseeker/) (MIT license)
and installation can be performed by running [pip](https://docs.python.org/es/3/installing/index.html):
```
python -m pip install codeseeker
```

To upgrade the package to the latest version:
```
python -m pip install codeseeker --upgrade
```

To delete the package:
```
python -m pip uninstall codeseeker
```

## Command Line Usage

The basic syntax for performing a search with `CodeSeeker` is:

```sh
codeseeker <keyword> [-r REPOSITORY] [-l LANGUAGE]
```

Where:

- `<keyword>` is the required search term.
- `-r REPOSITORY` (optional) specifies a GitHub repository in the format `owner/repo`.
- `-l LANGUAGE` (optional) specifies the programming language to filter by.

### Parameters

|Parameter|Shorthand|Default value|Description|
|---|---|---|---|
|keyword|(required)|None|The term to search for in code files|
|repository|`-r`|AyudaEnPython/Soluciones|The GitHub repository to search within|
|language|`-d`|python|The programming language to filter by|

## Example

To search for a file that contains _"cube"_ in a repository:

    > python -m codeseeker cube
    1 file found.

    repository/path/to/file.py

To open the file in a web browser

    > python -m codeseeker cube -o
    1 file found.

    repository/path/to/file.py

    Opening in a web browser...

To get the file:

    > python -m codeseeker fibonacci --get
    soluciones/serie_fibonacci.py
    sololearn/python_core/code_project_72_Fibonacci.py
    soluciones/menu_ejercicios.py
    soluciones/menu_ejercicios_naive.py
    soluciones/fibonacci.py

    5 file(s) found(s).

    Downloading and creating file(s)...
    Done!

You can also use it like this:

    > codeseeker calendar -r python/cpython
    Lib/test/test_calendar.py
    Lib/calendar.py
    Lib/test/test_strftime.py
    Lib/_strptime.py
    Lib/zoneinfo/_zoneinfo.py
    Tools/scripts/mailerdaemon.py
    Lib/datetime.py
    Lib/email/_parseaddr.py
    Lib/test/test_imaplib.py
    Lib/imaplib.py
    Lib/mailbox.py
    Lib/http/server.py
    Lib/ssl.py
    Lib/http/cookiejar.py
    Lib/test/datetimetester.py

    15 file(s) found(s).

Help command:

    > codeseeker -h

or:

    > codeseeker --help


## Contribution

If you'd like to contribute, fork the repository, commit your changes to main branch
and send a pull request.
Make sure you add yourself to authors.