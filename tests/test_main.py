import unittest
from unittest.mock import patch
from src.main import download_album

class TestMain(unittest.TestCase):

    @patch('src.main.input', side_effect=['album_name'])
    @patch('src.jmcomic_client.download_album')
    def test_download_album(self, mock_download, mock_input):
        download_album()
        mock_download.assert_called_once_with('album_name')

if __name__ == '__main__':
    unittest.main()