import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(2, 'Python',200);'''
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")

    cursor.execute(insert)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
