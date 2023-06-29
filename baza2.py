import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite.db')

    query = '''
    CREATE TABLE SqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);'''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")

    # cursor.execute(query)
    # sql_connection.commit()

    cursor.executescript(sql_script)
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
