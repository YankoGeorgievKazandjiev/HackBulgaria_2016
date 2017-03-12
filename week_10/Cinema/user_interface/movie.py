import sqlite3
import sys
import os

sys.path.insert(0, os.path.abspath('../'))
from user_interface import projection
from settings import sql_creations_settings
from queries import manage_db_queries

class Movie:
    def __init__(self, movie_id, name, rating):
        self.id = movie_id
        self.name = name
        self.rating = rating
        self.projections = []
        self.add_projections()

    def add_projections(self):
        project = sql_creations_settings.execute(manage_db_queries.SHOW_PROJECTIONS, [self.id].fetchall())
        for index in project:
            self.projections.append(projection.Projection(*index))

    def print_projections(self):
        for index in self.projections:
            print(index)
