.. codeseeker documentation master file, created by
   sphinx-quickstart on Tue Feb  1 01:36:19 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to codeseeker's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

::

                   .                 .
         ,-. ,-. ,-| ,-. ,-. ,-. ,-. | , ,-. ,-.
         |   | | | | |-' `-. |-' |-' |<  |-' |
         `-' `-' `-^ `-' `-' `-' `-' ' ` `-' '

``codeseeker`` is simple tool to search for code on Github.
By default it searches to the contents of the source code file.

Installation
------------

`codeseeker` is available on `PyPi <https://pypi.org/project/codeseeker/>`_ (MIT license)
and installation can be performed by running `pip <https://docs.python.org/es/3/installing/index.html>`_:


.. code-block:: console

   python -m pip install codeseeker

To upgrade the package to the latest version:

.. code-block:: console

   python -m pip install codeseeker --upgrade

To delete the package:

.. code-block:: console

   python -m pip uninstall codeseeker


Command Line Usage
------------------

The basic syntax for performing a search with `CodeSekeer` is:

.. code-block:: console

   codeseeker <keyword> [-r REPOSITORY] [-l LANGUAGE]

Where:

* ``keyword`` is the required search term.
* ``-r REPOSITORY`` (optional) specifies a GitHub repository in the format ``owner/repo``.
* ``-l LANGUAGE`` (optional) specifies the programming language to filter by.


Example
-------

To search for a file that contains *"cube"* in a repository:

.. code-block:: console

   > python -m codeseeker cube
   1 file found

   repository/path/to/file.python

To open the file in a web browser:

.. code-block:: console

   > python -m codeseeker cube -o
   1 file found.

   repository/path/to/file.py

   Opening in a web browser...

To get the file:

.. code-block:: console

   > python -m codeseeker fibonacci --get
   soluciones/serie_fibonacci.py
   sololearn/python_core/code_project_72_Fibonacci.py
   soluciones/menu_ejercicios.py
   soluciones/menu_ejercicios_naive.py
   soluciones/fibonacci.py

   5 file(s) found(s).

   Downloading and creating file(s)...
   Done!

You can use also use it like this:

.. code-block:: console

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

.. code-block:: console

   > codeseeker -h

or:

.. code-block:: console

   > codeseeker --help


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
