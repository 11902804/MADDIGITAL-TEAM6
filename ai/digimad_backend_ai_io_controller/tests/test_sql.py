import os
import mysql.connector
from dotenv import load_dotenv   # for python-dotenv method
load_dotenv()                    # for python-dotenv method


def connect_to_database():
    # os environments are defined in .env file
    return mysql.connector.connect(host=os.environ.get('HOST'),
                                   user=os.environ.get('USER'),
                                   password=os.environ.get('PASSWORD'),
                                   database=os.environ.get('DATABASE'))


def test_create_color():
    test_val = ("blue", "#123458")

    database = connect_to_database()
    database_cursor = database.cursor()

    database_cursor.execute("INSERT INTO colors (color_name, hex_value) \
                             VALUES (%s, %s)", test_val)

    assert database_cursor.rowcount == 1


def test_get_all_colors():
    database1 = connect_to_database()
    database_cursor1 = database1.cursor()
    database_cursor1.execute("SELECT * FROM colors")
    expected_rows = len(database_cursor1.fetchall())

    database2 = connect_to_database()
    database_cursor2 = database2.cursor()
    database_cursor2.execute("SELECT COUNT(*) FROM colors")
    # comma after actual_rows to unpack tuple of database response
    actual_rows, = database_cursor2.fetchone()

    assert expected_rows == actual_rows
