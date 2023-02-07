from answer3 import *
from psycopg2 import connect, OperationalError, ProgrammingError


USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "postgres"


def execute_sql(sql_code, db):
    """
    Run given sql code with psycopg2.
    :param str sql_code: sql code to run
    :param str db: name of db,
    :rtype: list
    :return: data from psycopg2 cursor as a list (can be None) if nothing to fetch.
    """
    # Place exercise 2 solution here.
    conn = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=db
    )

    with conn.cursor() as x:
        x.execute(sql_code)
        conn.commit()
        try:
            res = x.fetchall()
        except ProgrammingError:
            res = None

    return res


# print(execute_sql(query_1, 'exam'))
# print(execute_sql(query_3, 'exam'))
# print(execute_sql(query_2, 'exam'))
# print(execute_sql(query_4, 'exam'))
# print(execute_sql(query_5, 'exam'))
# print(execute_sql(query_6, 'exam'))
# print(execute_sql(query_7, 'exam'))  # Nie ma takiej książki, więc rzuca błąd
# print(execute_sql(query_8, 'exam'))
# print(execute_sql(query_9, 'exam'))
# print(execute_sql(query_10, 'exam'))
