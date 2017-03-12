SHOW_ALL_MOVIES = '''SELECT * FROM MOVIES
    ORDER BY RATING DESC'''

SHOW_PROJECTIONS = '''SELECT * FROM PROJECTIONS
    WHERE movie_id = ?
    ORDER BY movie_date'''

SHOW_PROJECTIONS_ON_DATE = '''SELECT * FROM PROJECTIONS
    WHERE movie_id = ?
    AND movie_date = ?
    ORDER BY movie_date'''

MOVIE_NAME_FROM_ID = '''SELECT name FROM MOVIES
    WHERE id = ?'''

CHECK_IF_USER_EXISTS = '''SELECT * FROM USERS
    WHERE USERNAME = ?'''

INSERT_INTO_USERS = '''INSERT INTO USERS (USERNAME, PASSWORD)
    VALUES (?, ?)'''

SELECT_USER = '''SELECT * FROM USERS
    WHERE USERNAME = ?'''

MOVIE_FROM_ID = '''SELECT * FROM MOVIES
    WHERE id = ?'''
