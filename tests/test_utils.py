import io
import unittest
from unittest.mock import patch
from textwrap import dedent

from codeseeker.utils import show


class TestCodeSeekerUtils(unittest.TestCase):

    def test_show(self):
        data = [
            {"path": "repository/path/to/file.py"},
            {"path": "repository/path/to/file2.py"},
        ]
        expected = dedent("""\
            repository/path/to/file.py
            repository/path/to/file2.py

            2 file(s) found(s).\n"""
        )
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            show(data)
            self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()