import io
import unittest
from unittest.mock import patch, Mock

from codeseeker.validators import validate_response, validate_data_links


class TestCodeSeekerException(unittest.TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected, mock_stdout, function=None):
        if function:
            function()
        self.assertEqual(mock_stdout.getvalue(), expected)
    
    @patch("codeseeker.seeker.requests.get")
    def test_validate_response(self, mock):
        mock = Mock(status_code=404)
        with self.assertRaises(Exception) as msg:
            validate_response(mock)
        self.assertEqual("Error: 404", str(msg.exception))

    def test_validate_data_links(self):
        data = []
        with self.assertRaises(Exception) as msg:
            validate_data_links(data)
        self.assertEqual(
            "Can't open in a web browser (there are no results).",
            str(msg.exception)
        )


if __name__ == '__main__':
    unittest.main()