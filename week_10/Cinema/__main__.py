import sqlite3
import os
import sys

sys.path.insert(0, os.path.abspath('./Cinema'))
from queries import create_db_queries
from settings import sql_creations_settings
from user_interface import user, interface, projection


def main():
    # sql_creations_settings.cursor.execute(create_db_queries.DROP_TABLES_MOVIES)
    # sql_creations_settings.cursor.execute(create_db_queries.CREATE_MOVIES_TABLE)
    # sql_creations_settings.cursor.execute(create_db_queries.DROP_TABLES_PROJECTIONS)
    # sql_creations_settings.cursor.execute(create_db_queries.CREATE_PROJECTIONS_TABLE)
    # sql_creations_settings.cursor.execute(create_db_queries.DROP_TABLES_USERS)
    # sql_creations_settings.cursor.execute(create_db_queries.CREATE_USERS_TABLE)
    # sql_creations_settings.cursor.execute(create_db_queries.DROP_TABLES_RESERVATIONS)
    # sql_creations_settings.cursor.execute(create_db_queries.CREATE_RESERVATIONS_TABLE)
    #
    # for movie in create_db_queries.MOVIES:
    #     sql_creations_settings.cursor.execute(create_db_queries.INSERT_MOVIES, movie)
    #
    # for projections in create_db_queries.PROJECTIONS:
    #     sql_creations_settings.cursor.execute(create_db_queries.INSERT_PROJECTIONS, projections)
    #
    # sql_creations_settings.connection.commit()
    # sql_creations_settings.connection.close()

    inter = interface.Interface()
    # inter = projection.Projection.available_seats
    # print(inter)
    # inter.show_start_menu()

if __name__ == '__main__':
    main()
