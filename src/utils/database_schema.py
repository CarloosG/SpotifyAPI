from sqlalchemy import create_engine, text
from src.handler.spotify_handler import SpotifyHandler
import sqlalchemy

class DatabaseSchema:
    def __init__(self,spotify):
        self.spotify = spotify


        def create_star_schema():
            schema_sql = """
            CREATE TABLE IF NOT EXISTS dim_artista (
                artist_id TEXT PRIMARY KEY,
                artist_name TEXT,
                artist_popularity INTEGER,
                artist_followers BIGINT,
                genres TEXT,
                type TEXT
            );

            CREATE TABLE IF NOT EXISTS dim_album (
                album_id TEXT PRIMARY KEY,
                album_name TEXT,
                release_date DATE,
                total_tracks INTEGER,
                artists TEXT
            );

            CREATE TABLE IF NOT EXISTS dim_genero (
                genre_id TEXT PRIMARY KEY,
                genre_name TEXT,
                genre_popularity INTEGER,
                genre_followers BIGINT
            );

            CREATE TABLE IF NOT EXISTS dim_tiempo (
                date_id INTEGER PRIMARY KEY,  -- formato YYYYMMDD
                release_date DATE,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                quarter INTEGER,
                day_of_week INTEGER
            );

            CREATE TABLE IF NOT EXISTS dim_playlist (
                playlist_id TEXT,
                track_id TEXT,
                playlist_added_at TIMESTAMP,
                release_date DATE,
                track_album_id TEXT,
                track_album_name TEXT,
                track_album_artists TEXT,
                track_album_total_tracks INTEGER,
                track_artists TEXT,
                track_name TEXT,
                track_duration_ms INTEGER,
                popularity INTEGER,
                track_explicit BOOLEAN,
                PRIMARY KEY (playlist_id, track_id)
            );

            CREATE TABLE IF NOT EXISTS fact_tracks (
                track_id TEXT PRIMARY KEY,
                track_name TEXT,
                track_duration INTEGER,
                track_explicit BOOLEAN,
                release_date DATE,
                artist_id TEXT,
                album_id TEXT,
                date_id INTEGER,
                popularity INTEGER,
                track_album TEXT,

                FOREIGN KEY (artist_id) REFERENCES dim_artista(artist_id),
                FOREIGN KEY (album_id) REFERENCES dim_album(album_id),
                FOREIGN KEY (date_id) REFERENCES dim_tiempo(date_id)
            );
            """
            with self.spotify.engine.begin() as conn:
                conn.execute(text(schema_sql))
                print("✅ Esquema Star Schema creado exitosamente.")


