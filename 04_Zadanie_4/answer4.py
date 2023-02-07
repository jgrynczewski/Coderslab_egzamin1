from flask import Flask, request
from psycopg2 import connect, ProgrammingError
from psycopg2.extensions import AsIs


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


app = Flask(__name__)


form = """
    <html>
        <head>
        </head>
        <body>
            <form method='POST'>
                <input type='text' name='name' placeholder='name'>
                <input type='email' name='email' placeholder='email'>
                <input type='submit' value='Zapisz'>
            </form>
        </body>
    </html>
"""


@app.route("/reader/add/", methods=['GET', 'POST'])
def create_reader():
    if request.method == "GET":
        return form

    elif request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')

        if name and '@' in email:
            sql = f"""
            INSERT INTO Readers (name, email)
            VALUES ('{AsIs(name)}', '{AsIs(email)}')
            """
            execute_sql(sql, 'exam')
            return "Pomyślnie zapisane czytelnika do bazy"

        else:
            return "Wystąpił błąd. W formularzu wprowadzono nieprawidłową wartość."


if __name__ == "__main__":
    app.run()