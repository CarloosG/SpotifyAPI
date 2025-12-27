import sqlalchemy
from src.constants.general import SpotifyConstants, DockerConstants

class PostgreSQLHandler:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PostgreSQLHandler, cls).__new__(cls)
            print("New instance created")
        return cls._instance
    def __init__(self,dockerConstants):
        if not hasattr(self, "_initialized"):
            print("inicializing object engine")
            self.docker_constants= dockerConstants
            self.engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{self.docker_constants.POSTGRES_USER}:{self.docker_constants.POSTGRES_PASSWORD}@postgres:5432/{self.docker_constants.POSTGRES_DB}")
            self._initialized = True
