import sys
import os
import sqlite3
import getpass
sys.path.insert(0, os.path.abspath('../'))
from user_interface import user
from user_interface import movie
from user_interface import projection
from settings import sql_creation_settings
from settings import general_settings
from queries import manage_db_queries


class Interface:
    def __init__(self):
        self.conn = sqlite3.connect(sql_creation_settings.DATABASE_NAME)
        self.c = self.conn.cursor()
        self.user = None
        self.movies = []
        self.add_movies()
        self.show_start_menu()

    def show_start_menu(self):
        print(general_settings.INITIAL_GREETING)
        decision = input()
        if decision == "exit":
            os.system('clear')
            print(general_settings.GOODBYE)
            return
        elif decision == "logout":
            os.system('clear')
            self.logout()
            self.show_start_menu()
        elif decision == "help":
            os.system('clear')
            print(general_settings.HELP)
            self.show_start_menu()
        elif decision == "show movies":
            os.system('clear')
            self.show_movies()
            self.show_start_menu()
        elif "show movie projections" in decision:
            os.system('clear')
            movie_id = decision.split(' ')[3]
            date = None
            if len(decision.split(' ')) > 4:
                date = decision.split(' ')[4]
            if date:
                self.show_movie_projections(movie_id, str(date))
            else:
                self.show_movie_projections(movie_id)
            self.show_start_menu()
        elif decision == "make reservation":
            os.system('clear')
            self.make_reservation()

    def add_movies(self):
        db_movies = self.c.execute(manage_db_queries.SHOW_ALL_MOVIES).fetchall()
        for db_movie in db_movies:
            self.movies.append(movie.Movie(*db_movie))

    def show_movies(self):
        print(general_settings.MOVIES_INFO)
        movies = self.c.execute(manage_db_queries.SHOW_ALL_MOVIES).fetchall()
        for movie in movies:
            print(movie)

    def show_movie_projections(self, movie_id, date=None):
        m_name = self.c.execute(manage_db_queries.MOVIE_NAME_FROM_ID, [movie_id]).fetchall()[0][0]
        if date == None:
            print(general_settings.PROJECTIONS_INFO.format(m_name))
            projections = self.c.execute(manage_db_queries.SHOW_PROJECTIONS, [movie_id]).fetchall()
        else:
            print(general_settings.PROJECTIONS_ON_DATE_INFO.format(m_name, date))
            projections = self.c.execute(manage_db_queries.SHOW_PROJECTIONS_ON_DATE, [movie_id, date]).fetchall()
        for projection in projections:
            print(projection)

    def make_reservation(self):
        self.check_login_status()
        print(general_settings.CHOOSE_NUM_TICKETS)
        inpt = input()
        if inpt == "give up":
            self.show_start_menu()
        elif inpt.isdigit():
            self.manage_movie(int(inpt))
        else:
            self.make_reservation()

    def manage_movie(self, num_reservations):
            self.show_movies()
            print(general_settings.CHOOSE_MOVIE)
            inpt = input()
            if input == "give up":
                self.show_start_menu()
            elif not inpt.isdigit():
                self.show_movies(num_reservations)
            else:
                mv_idx = int(inpt) - 1
                movie = self.movies[mv_idx]
                self.manage_projections(num_reservations, movie)

    def manage_projections(self, num_reservations, movie):
        print(general_settings.PROJECTIONS_FOR_MOVIE.format(movie.name))
        movie.print_projections()
        print(general_settings.CHOOSE_PROJECTION)
        inpt = input()
        if inpt == "give up":
            self.show_start_menu()
        elif not inpt.isdigit():
            self.manage_projections(num_reservations, movie)
        else:
            projection = movie.projections[int(inpt) - 1]
            self.manage_seats(num_reservations, projection)

    def manage_seats(self, num_reservations, prjctn):
        seats = []
        for r in range(num_reservations):
            print(general_settings.AVAILABLE_SEATS_MESSAGE)
            prjctn.print_seats()
            print(general_settings.CHOOSE_SEAT_MESSAGE.format(r + 1))
            inpt = input()
            if inpt == "give up":
                self.show_start_menu()
            else:
                coordinates = [int(x) for x in inpt.split(', ')]
                while not prjctn.try_reserve_seat(coordinates):
                    print(general_settings.AVAILABLE_SEATS_MESSAGE)
                    prjctn.print_seats()
                    print(general_settings.CHOOSE_SEAT_MESSAGE.format(r + 1))
                    inpt = input()
                    if inpt == "give up":
                        self.show_start_menu()
                    coordinates = [int(x) for x in inpt.split(', ')]
                seats.append(coordinates)
        print(general_settings.AVAILABLE_SEATS_MESSAGE)
        prjctn.print_seats()
        print(general_settings.CONFIRM_RESERVATION)
        self.finalize(prjctn, seats)
