import os
import requests
from constants.general import SpotifyConstants
from utils.requester import Requester


class SpotifyHandler:
        _instance = None
        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super(SpotifyHandler, cls).__new__(cls)
            return cls._instance
        
        def __init__(self):
            if not hasattr(self, "_initialized"):
                self.constants = SpotifyConstants() 
                self.token_url = self.constants.TOKEN_URL  
                self.base_url = "https://api.spotify.com/v1"  
                self.requester = Requester(max_retries=5, backoff_factor=2)
                self.header_token = self.get_token()
                self.headers = {"Authorization": f"Bearer {self.header_token}"}  
                self._initialized = True

        def get_token(self):
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = {
                "grant_type": "client_credentials",
                "client_id": self.constants.CLIENT_ID,
                "client_secret": self.constants.CLIENT_SECRET,
            }
            response = self.requester.post(self.token_url, headers=headers)

        def get_artist(self, artist_id: str):
            url = f"{self.base_url}/artists/{artist_id}"
            response = self.requester.get(url, headers=self.headers)
            return response.json()   
            
        def get_artist_music(self, artist_id:str):
            url=f"{self.base_url}/artist/{artist_id}/albums"
            response = self.requester.get(url, headers=self.headers)
            return response.json()  
        
        def get_song(self, song_id:str):
            url=f"{self.base_url}/tracks/{song_id}"
            response = self.requester.get(url, headers=self.headers)
            return response.json()
        
        def get_playlist(self, playlist_id: str):
            url = f"{self.base_url}/playlists/{playlist_id}"
            response = self.requester.get(url, headers=self.headers)
            return response.json()
        
        def get_country_new_releases(self, country_id:str):
            url=f"{self.base_url}/browse/new-releases?country={country_id}"
            response = self.requester.get(url, headers=self.headers)
            return response.json()
        

        def search_artists_by_genre(self, genre: str, market: str = "CO", limit: int = 50):
            params = {
                "q": f"genre:{genre}",
                "type": "artist",
                "market": market,
                "limit": limit
            }
            url = f"{self.base_url}/search"
            response = self.requester.get(url, headers=self.headers, params=params)
            return response.json()


