from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SpotifyConstants:
    CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET")
    TOKEN_URL: str = os.getenv("SPOTIFY_TOKEN_URL")
    BASE_URL: str = "https://api.spotify.com/v1"

