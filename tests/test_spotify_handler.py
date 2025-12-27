
import pytest
import unittest
from src.handler.spotify_handler import SpotifyHandler
from unittest.mock import patch, Mock


class TestSpotifyHandler(unittest.TestCase):
    @patch.object(SpotifyHandler, 'get_token', return_value='fake_token')
    @patch('src.utils.requester.Requester.get')
    def test_get_artist(self, mock_get, mock_get_token):
        mock_response = Mock()
        response_dict = {'id':'123','name':'Test Artist','genres':['pop'],'followers':{'total':1000},'popularity':50}
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response

        spotify_handler = SpotifyHandler(Mock(), Mock())
        artist_data = spotify_handler.get_artist('123')

        mock_get.assert_called_once_with('https://api.spotify.com/v1/artists/123', headers=spotify_handler.headers)
        self.assertEqual(artist_data, response_dict)

if __name__ == '__main__':
    unittest.main()




        # mock_response = Mock()
        # expected_json = {'id': '123', 'name': 'Test Artist'}
        # mock_response.json.return_value = expected_json
        # mock_get.return_value = mock_response

        # spotify_handler = SpotifyHandler(Mock(), Mock())
        # result = spotify_handler.get_artist('123')

        # self.assertEqual(result, expected_json)
        # mock_get.assert_called_once_with(f"{spotify_handler.base_url}/artists/123", headers=spotify_handler.headers)



