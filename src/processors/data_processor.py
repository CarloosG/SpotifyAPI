import sys
import os
import pandas as pd 
import sqlalchemy
from pandas.io.json import json_normalize
import json
import psycopg2
from sqlalchemy import inspect
from src.handler.spotify_handler import SpotifyHandler
from datetime import datetime






sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class dataProcessor:
    def __init__(self,spotify):
        self.spotify = spotify


    def process_songs_and_time(self,songs:list): #ok
        df = pd.DataFrame()
        for song in songs:
            sngs = self.spotify.get_song(song)
            sngs = pd.json_normalize(sngs, sep="_")
            df = pd.concat([df,sngs])
        df['artist_id'] = df['artists'].apply(
            lambda artists: artists[0]['id'] if isinstance(artists, list) and artists else None
        )


        df = df.drop([ 'href', 'preview_url','uri','album_external_urls_spotify', 'album_href', 'album_images','album_uri', 'external_ids_isrc',
            'external_urls_spotify','available_markets','is_local','type','album_album_type','album_release_date_precision','album_total_tracks','album_type','album_available_markets','track_number','disc_number','artists','album_artists'],axis=1)
        df = df.rename(columns={
             'id': 'track_id',
             'name': 'track_name',
             'duration_ms': 'track_duration',
             'explicit': 'track_explicit',
             'album_name': 'track_album',
             'album_release_date': 'release_date'
         })
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        #dim tiempo
        dim_tiempo = df[['release_date']].drop_duplicates().dropna()
        dim_tiempo['year'] = dim_tiempo['release_date'].dt.year
        dim_tiempo['month'] = dim_tiempo['release_date'].dt.month
        dim_tiempo['day'] = dim_tiempo['release_date'].dt.day
        dim_tiempo['quarter'] = dim_tiempo['release_date'].dt.quarter
        dim_tiempo['day_of_week'] = dim_tiempo['release_date'].dt.dayofweek
        dim_tiempo['date_id'] = dim_tiempo['release_date'].dt.strftime('%Y%m%d').astype(int)
        dim_tiempo.to_sql('dim_tiempo', self.spotify.engine, if_exists='append', index=False)
        df['date_id'] = df['release_date'].dt.strftime('%Y%m%d').astype(int)
        df.to_sql('fact_tracks', self.spotify.engine, if_exists='append', index=False)


    def procces_artists(self,artists:list): #ok
        df = pd.DataFrame()
        for artist in artists:
            art = self.spotify.get_artist(artist)
            art = pd.json_normalize(art,sep="_")
            df = pd.concat([df,art])
        df = df.drop(['href','uri','external_urls_spotify', 'followers_href','images'],axis=1)
        df = df.rename(columns={
            'id': 'artist_id',
            'name': 'artist_name',
            'popularity': 'artist_popularity',
            'followers_total': 'artist_followers'
        })
        df.to_sql('dim_artista', self.spotify.engine, if_exists='append', index=False)

    
    
    def process_albums(self,country_releases:list,artist_music:list): #ok
        df_music = pd.DataFrame()
        for music in artist_music:
            msc = self.spotify.get_artist_music(music)
            items = msc["items"]
            df_msc = pd.json_normalize(items, sep="_")
            df_music = pd.concat([df_music,df_msc])
            df_music = df_music.drop(['href','images','uri','external_urls_spotify','available_markets','type','release_date_precision','album_group','album_type'],axis=1)
        df_country = pd.DataFrame()
        for country in country_releases:
            ctry = self.spotify.get_country_new_releases(country)
            ctry = ctry["albums"]["items"]
            ctry = pd.json_normalize(ctry, sep="_")
            df_country = pd.concat([df_country,ctry])
            df_country = df_country.drop([ 'href','images','type', 'uri', 'external_urls_spotify','available_markets','release_date_precision','album_type'],axis=1)
        df = pd.concat([df_music, df_country])
        df = df.drop_duplicates(subset='id')
        df['artists'] = df['artists'].apply(
            lambda x: ', '.join([artist['name'] for artist in x]) if isinstance(x, list) else ''
        )
        df = df.rename(columns={
            'id': 'album_id',
            'name': 'album_name',
            'release_date': 'release_date',
            'total_tracks': 'total_tracks',
            'artists': 'artists'
        })
        df.to_sql('dim_album', self.spotify.engine, if_exists='append', index=False)

    
    
    def procces_playlist(self,playlists:list) :#ok
        df = pd.DataFrame()
        for playlist in playlists:
            ply = self.spotify.get_playlist(playlist)
            items = ply["tracks"]["items"]
            df_ply = pd.json_normalize(items,sep="_")
            df_ply['playlist_id'] = playlist

            df = pd.concat([df,df_ply])    
        df = df.drop(['is_local','is_local','added_by_external_urls_spotify', 'added_by_href','added_by_uri', 'track_preview_url','track_album_album_type', 'track_album_href','track_album_images', 'track_album_uri','track_album_external_urls_spotify','track_external_ids_isrc',
       'track_external_urls_spotify', 'track_href','track_uri', 'track_is_local','video_thumbnail_url','primary_color','added_by_id','added_by_type','track_available_markets','track_type','track_episode','track_track','track_album_available_markets','track_album_type','track_album_release_date_precision','track_disc_number','track_track_number'],axis=1)
        df = df.rename(columns={
             'track_popularity': 'popularity',
             'track_album_release_date': 'release_date',
             'added_at': 'playlist_added_at'
         })

        df['track_artists'] = df['track_artists'].apply(
            lambda x: ', '.join([artist['name'] for artist in x]) if isinstance(x, list) else ''
        )
        df['track_album_artists'] = df['track_album_artists'].apply(
            lambda artists: ', '.join([artist['name'] for artist in artists]) if isinstance(artists, list) else ''
        )
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        df['playlist_added_at'] = pd.to_datetime(df['playlist_added_at'], errors='coerce')
        df.to_sql('dim_playlist', self.spotify.engine, if_exists='append', index=False)

        
    
    def process_genre(self,genres:list):#ok
        df = pd.DataFrame()
        for genre in genres:
            gnr = self.spotify.search_artists_by_genre(genre)         
            items = gnr["artists"]["items"]
            df_gnr = pd.json_normalize(items, sep="_")
            df = pd.concat([df,df_gnr]) 
        df = df.drop(['href','images','type', 'uri','external_urls_spotify', 'followers_href','genres'],axis=1)              
        df = df.rename(columns={
            'id': 'genre_id',
            'name': 'genre_name',
            'popularity': 'genre_popularity',
            'followers_total': 'genre_followers'
        })
        df.to_sql('dim_genero', self.spotify.engine, if_exists='append', index=False)

    

