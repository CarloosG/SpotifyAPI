import os
import requests
from dotenv import load_dotenv

class SpotifyHandler:
        def __init__(self):
            load_dotenv()  
            self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
            self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
            self.token_url = os.getenv("SPOTIFY_TOKEN_URL")
            self.base_url = "https://api.spotify.com/v1"
            self.headers = {"Authorization": f"Bearer {self.get_token()}"}

        def get_token(self):
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            response = requests.post(self.token_url, headers=headers, data=data)
            if response.status_code == 200:
                token = response.json().get("access_token")
                return token
            else:
                raise Exception(f"Error al obtener el token: {response.status_code} - {response.text}")
        
        def get_artist(self, artist_id: str):
            url = f"{self.base_url}/artists/{artist_id}"
            response = requests.get(url, headers=self.headers)
            return response.json()   
            
        def get_artist_music(self, artist_id:str):
            url=f"{self.base_url}/artist/{artist_id}/albums"
            response = requests.get(url, headers=self.headers)
            return response.json()  
        
        def get_song(self, song_id:str):
            url=f"{self.base_url}/tracks/{song_id}"
            response = requests.get(url, headers=self.headers)
            return response.json()
        
        def get_playlist(self, playlist_id: str):
            url = f"{self.base_url}/playlists/{playlist_id}"
            response = requests.get(url, headers=self.headers)
            return response.json()
        
        def get_country_new_releases(self, country_id:str):
            url=f"{self.base_url}/browse/new-releases?country={country_id}"
            response = requests.get(url, headers=self.headers)
            return response.json()
        

        def search_artists_by_genre(self, genre: str, market: str = "CO", limit: int = 50):
            params = {
                "q": f"genre:{genre}",
                "type": "artist",
                "market": market,
                "limit": limit
            }
            url = f"{self.base_url}/search"
            response = requests.get(url, headers=self.headers, params=params)
            return response.json()


