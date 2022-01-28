import io
import unittest
from unittest.mock import patch, Mock

from codeseeker.codeseeker import validate_response

class TestCodeSeekerException(unittest.TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected, mock_stdout, function=None):
        if function:
            function()
        self.assertEqual(mock_stdout.getvalue(), expected)
    
    @patch("codeseeker.codeseeker.requests.get")
    def test_validate_response(self, mock):
        mock = Mock(status_code=404)
        with self.assertRaises(Exception) as msg:
            validate_response(mock)
        self.assertEqual("Error: 404", str(msg.exception))


if __name__ == '__main__':
    unittest.main()