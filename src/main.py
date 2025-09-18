from src.handler.spotify_handler import SpotifyHandler
from src.handler.postgresql_handler import PostgreSQLHandler
from src.processors.data_processor import dataProcessor
from src.utils.database_schema import DatabaseSchema
from src.constants.general import SpotifyConstants, DockerConstants
from src.utils.cli  import cli
import pandas as pd


if __name__ == "__main__":
        dockerConstants = DockerConstants()
        pg_handler = PostgreSQLHandler(dockerConstants)
        spotifyConstants = SpotifyConstants()
        spotify = SpotifyHandler(spotifyConstants, pg_handler.engine)  
        dataProcessor = dataProcessor(spotify)
        cli = cli(dataProcessor)
        cli.parser()

