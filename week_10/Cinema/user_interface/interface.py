import sqlite3
import os
import getpass
import sys

sys.path.insert(0, os.path.abspath('../'))
from user_interface import user, movie, projection
from settings import sql_creations_settings, general_settings
from queries import manage_db_queries

class Interface:
    def __init__(self):
        self.user = None
        self.movies = []
        # self.add_movies()
        self.show_start_menu()

    def show_start_menu(self):
        print(general_settings.INITIAL_GREETING)
        decision = input()
        if decision == "5":
            os.system('clear')
            sql_creations_settings.cursor.close()
            print(general_settings.GOODBYE)
            return
        elif decision == "logout":
            os.system('clear')
            self.logout()
            self.show_start_menu()
        elif decision == "6":
            os.system('clear')
            print(general_settings.HELP)
            self.show_start_menu()
        elif decision == "1":
            os.system('clear')
            self.show_movies()
            self.show_start_menu()
        elif decision == "2":
            os.system('clear')
            print("Enter id and date(like:2014-04-01):\n")
            decision2 = input()
            movie_id = decision2.split(' ')[0]
            date = None
            if len(decision2.split(' ')) > 1:
                date = decision2.split(' ')[1]
            if date:
                self.show_movie_projections(movie_id, str(date))
            else:
                self.show_movie_projections(movie_id)
            self.show_start_menu()
        elif decision == "3":
            os.system('clear')
            self.make_reservation()

    def add_movies(self):
        db = sql_creations_settings.cursor.execute(create_db_queries.INSERT_MOVIES).fetchall()
        for index in db:
            self.movies.append(movie.Movie(*index))

    def show_movies(self):
        print(general_settings.MOVIES_INFO)
        movies = sql_creations_settings.cursor.execute(manage_db_queries.SHOW_ALL_MOVIES).fetchall()
        for index in movies:
            print(index)

    def show_movie_projections(self, movie_id, date = None):
        movie_name = sql_creations_settings.cursor.execute(manage_db_queries.MOVIE_NAME_FROM_ID, [movie_id]).fetchall()[0][0]
        if date == None:
            print(general_settings.PROJECTIONS_INFO.format(movie_name))
            projections = sql_creations_settings.cursor.execute(manage_db_queries.SHOW_PROJECTIONS, [movie_id]).fetchall()
        else:
            print(general_settings.PROJECTIONS_ON_DATE_INFO.format(movie_name, date))
            projections = sql_creations_settings.cursor.execute(manage_db_queries.SHOW_PROJECTIONS_ON_DATE, [movie_id, date]).fetchall()
        for index in projections:
            print(index)

    def make_reservation(self):
        self.login_status()
        print(general_settings.CHOOSE_NUM_TICKETS)
        decision = input()
        if decision == "exit()":
            self.show_start_menu()
        elif decision.isdigit():
            self.manage_movie(int(decision))
        else:
            self.make_reservation()

    def login_status(self):
        if not self.user:
            print(general_settings.RESERVATION_ATTEMPT_MESSAGE)
            print(general_settings.RESERVATION_LOGIN_MENU)
            inp = input()
            while inp != "1" and inp != "2":
                print(general_settings.RESERVATION_LOGIN_MENU)
                inp = input()
            if inp == "1":
                self.registrate_new_user()
            else:
                self.login()

        print(general_settings.USER_GREETING.format(self.user.username))

    def registrate_new_user(self):
        self.user = user.User()
        self.validate_new_username()
        self.validate_new_password()
        hashed_pass = user.User.hash_string(self.user.password)
        res = sql_creations_settings.cursor.execute(manage_db_queries.INSERT_INTO_USERS, [self.user.username, hashed_pass])
        sql_creations_settings.connection.commit()
        print(general_settings.SUCCESSFUL_REGISTRATION)

    def validate_new_username(self):
        print(general_settings.CHOOSE_USERNAME)
        username = input()
        all_usernames = sql_creations_settings.cursor.execute(manage_db_queries.CHECK_IF_USER_EXISTS, [username]).fetchall()
        if len(all_usernames) != 0:
            print(general_settings.USERNAME_EXIST)
            self.registrate_new_user()
        self.user.username = username

    def validate_new_password(self):
        password = getpass.getpass()
        print(general_settings.CHOOSE_PASSWORD)
        while not self.user.set_pass(password):
            print(general_settings.PASSWORD_REQUIREMENTS)
            password = getpass.getpass()

        print(general_settings.REPEAT_PASSWORD)
        pass2 = getpass.getpass()
        while password != pass2:
            print(general_settings.REPEAT_PASSWORD)
            pass2 = getpass.getpass()

    def login(self):
        self.user = user.User()
        self.find_if_user_exist()
        self.validate_pass()
        print(general_settings.SUCCESSFUL_LOGIN)

    def find_if_user_exist(self):
        print(general_settings.SELECT_USERNAME)
        username = input()
        all_usernames = sql_creations_settings.cursor.execute(manage_db_queries.SELECT_USER, [username]).fetchall()
        while len(all_usernames) == 0:
            print(general_settings.USERNAME_DOES_NOT_EXIST)
            username = input()
            all_usernames = sql_creations_settings.cursor.execute(manage_db_queries.SELECT_USER, [username]).fetchall()
        self.user.username = username

    def validate_pass(self):
        all_usernames = sql_creations_settings.cursor.execute(manage_db_queries.SELECT_USER, [self.user.username]).fetchall()
        user_pass = all_usernames[0][2]
        password = getpass.getpass()
        hashed_pass =user.User.hash_string(password)

        while hashed_pass != user_pass:
            password = getpass.getpass()
            hashed_pass = user.User.hash_string(password)
        self.user.password = hashed_pass

    def manage_movie(self, num_tickets):
        self.show_movies()
        print(general_settings.CHOOSE_MOVIE)
        inpt = input()
        if inpt == "exit()":
            self.show_start_menu()
        elif not inpt.isdigit():
            self.show_movies()
        else:
            movie_index = int(inpt) - 1
            movie = self.movies[movie_index]
            self.manage_projections(num_tickets)


    # def shema(func):
    #     def decorated(self,projection, seats):
    #         db = sql_creations_settings.cursor.execute(manage_db_queries.MOVIE_FROM_ID, [projection.movie_id]).fetchall()[0]
    #         movie = movie.Movie(*db)
    #         print(general_settings.RESERVATION_SUMMARY.format(movie.name, movie.rating, projection.date, projection.time, projection.type, seats))
    #         return func(self, projection, seats)
    #     return decorated
    #
    # @shema
    # def confirm(self, projection, seats):
    #     inpt = input()
    #     while inpt != "finalize":
    #         print(general_settings.CONFIRM_RESERVATION)
    #         inpt = input()
    #     self.show_start_menu()
