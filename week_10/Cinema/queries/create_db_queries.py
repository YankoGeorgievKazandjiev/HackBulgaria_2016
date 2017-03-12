DROP_TABLES_MOVIES = '''
        DROP TABLE IF EXISTS MOVIES
'''
DROP_TABLES_PROJECTIONS = '''
        DROP TABLE IF EXISTS PROJECTIONS
'''
DROP_TABLES_USERS = '''
        DROP TABLE IF EXISTS USERS
'''
DROP_TABLES_RESERVATIONS = '''
        DROP TABLE IF EXISTS RESERVATIONS
'''

CREATE_MOVIES_TABLE = '''CREATE TABLE "Movies" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "rating" TEXT NOT NULL
)'''

CREATE_PROJECTIONS_TABLE = '''CREATE TABLE "Projections" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "movie_id" INTEGER NOT NULL,
    "type" TEXT NOT NULL,
    "movie_date" TEXT NOT NULL,
    "movie_time" TEXT NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
)'''

CREATE_USERS_TABLE = '''CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT NOT NULL,
    "password" VARCHAR(50) NOT NULL
)'''

CREATE_RESERVATIONS_TABLE = '''CREATE TABLE "Reservations" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "projection_id" INTEGER NOT NULL,
    "row" INTEGER NOT NULL,
    "col" INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    FOREIGN KEY (projection_id) REFERENCES Projections(id)
)'''

INSERT_MOVIES = '''
    INSERT INTO MOVIES (name, rating)
    VALUES (?, ?)
'''

INSERT_PROJECTIONS = '''
    INSERT INTO PROJECTIONS (movie_id, type, movie_date, movie_time)
    VALUES (?, ?, ?, ?)
'''

MOVIES = [["The Hunger Games: Catching Fire", "7.9"], ["Wreck-It-Ralph", "7.8"], ["Her", "8.3"]]

PROJECTIONS = [[1, '3D','2014-04-01', "19:10"],
               [1, '2D','2014-04-01', "19:00"],
               [1, '4DX','2014-04-02', "21:00"],
               [3, '2D','2014-04-05', "20:20"],
               [2, '3D','2014-04-02', "22:00"],
               [2, '2D','2014-04-02', "19:30"]]
