import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
