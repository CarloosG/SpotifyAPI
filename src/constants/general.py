from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SpotifyConstants:
    CLIENT_ID: str = os.getenv("SPOTIFY_CLIENT_ID").strip()
    CLIENT_SECRET: str = os.getenv("SPOTIFY_CLIENT_SECRET").strip()
    TOKEN_URL: str = os.getenv("SPOTIFY_TOKEN_URL").strip()

class DockerConstants:
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD").strip()
    POSTGRES_USER: str = os.getenv("POSTGRES_USER").strip()
    POSTGRES_DB: str = os.getenv("POSTGRES_DB").strip()
    PG_ADMIN_EMAIL: str = os.getenv("PG_ADMIN_EMAIL").strip()
    PG_ADMIN_PASSWORD: str = os.getenv("PG_ADMIN_PASSWORD").strip()
