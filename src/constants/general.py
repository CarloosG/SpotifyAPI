from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SpotifyConstants:
    CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET")
    TOKEN_URL: str = os.getenv("SPOTIFY_TOKEN_URL")

class DockerConstants:
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    PG_ADMIN_EMAIL: str = os.getenv("PG_ADMIN_EMAIL")
    PG_ADMIN_PASSWORD: str = os.getenv("PG_ADMIN_PASSWORD")
