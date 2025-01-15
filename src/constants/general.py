from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SpotifyConstants:
    CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET")
    TOKEN_URL: str = os.getenv("SPOTIFY_TOKEN_URL")
    BASE_URL: str = "https://api.spotify.com/v1"



# SPOTIFY_CLIENT_ID="15c528e05d8947f8bcc3d60683421505"
# SPOTIFY_CLIENT_SECRET="7af4880026714be3a83441c3dddbe556"
# SPOTIFY_TOKEN_URL="https://accounts.spotify.com/api/token"
