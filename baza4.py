import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(2, 'Python',200);'''

    select = '''
    SELECT * FROM software;
    '''

    update = '''
    UPDATE software SET price = 2000 WHERE id=2;'''

    delete = '''
    DELETE FROM software WHERE id=2;'''
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")

    # wpisanie danych do bazy
    # cursor.execute(insert)
    # sql_connection.commit()

    # odczytanie danych z bazy
    for row in cursor.execute(select):
        print(row)  # (2, 'Python', 200.0)

    # cursor.execute(update)
    # sql_connection.commit()
    cursor.execute(delete)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
