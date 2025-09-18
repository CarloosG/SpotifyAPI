import sys
import os
import argparse
import pandas as pd 
import sqlalchemy
from pandas.io.json import json_normalize
import json
import psycopg2
from sqlalchemy import inspect
from src.handler.spotify_handler import SpotifyHandler
from src.processors.data_processor import dataProcessor




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class cli:
    def __init__(self,dataprocessor):
        self.processor = dataprocessor
  
    def parser(self):
            global_parser = argparse.ArgumentParser(description="Spotify Data Processor CLI")
            subparsers = global_parser.add_subparsers(title="subcommands", help="Get metadata from spotify API") 
            arg_template = {
                "metavar": "ITEM_ID",
                "help": "ID of the item to process",
                "type": str,
                "nargs": 1,
            }
            songs_parser = subparsers.add_parser("songs", help="Process songs metadata") #ok
            songs_parser.add_argument("songs", **arg_template)
            songs_parser.set_defaults(func=self.processor.process_songs_and_time)

            artist_parser = subparsers.add_parser("artists", help="Process artists metadata")#ok
            artist_parser.add_argument("artists", **arg_template)
            artist_parser.set_defaults(func=self.processor.procces_artists)

            album_parser = subparsers.add_parser("albums", help="Process albums metadata") #ok
            album_parser.add_argument("country",**arg_template)
            album_parser.add_argument("artist_music", **arg_template)
            album_parser.set_defaults(func=self.processor.process_albums)

            playlist_parser = subparsers.add_parser("playlist", help="Process playlist metadata")#ok
            playlist_parser.add_argument("playlist",**arg_template)
            playlist_parser.set_defaults(func=self.processor.procces_playlist)  

            genre_parser = subparsers.add_parser("genre", help="Process genre metadata") #so so
            genre_parser.add_argument("genre", **arg_template)
            genre_parser.set_defaults(func=self.processor.process_genre)

            args = global_parser.parse_args()
            if hasattr(args, "func"):
                if hasattr(args, "country") and hasattr(args, "artist_music"):
                    args.func(args.country, args.artist_music)
                else:
                    arg_name = [k for k in vars(args) if k not in ("func",)][0]
                    args.func(getattr(args, arg_name))
            else:
                    global_parser.print_help()



