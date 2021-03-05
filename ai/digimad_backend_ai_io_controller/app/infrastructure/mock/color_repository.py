import os
import mysql.connector
from dotenv import load_dotenv   # for python-dotenv method
load_dotenv()                    # for python-dotenv method


class ColorRepository:
    # if you have trouble connecting with databse check readme
    def connect_to_database(self):
        # os environments are defined in .env file
        return mysql.connector.connect(host=os.environ.get('HOST'),
                                       user=os.environ.get('USER'),
                                       password=os.environ.get('PASSWORD'),
                                       database=os.environ.get('DATABASE'))

    def create(self, color_name: str, hex_value: str):
        try:
            val = (color_name, hex_value)

            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("INSERT INTO colors (color_name, hex_value) \
                            VALUES (%s, %s)", val)

            database.commit()

            message = "{} rows inserted!".format(database_cursor.rowcount)
            return {"message": message}
        except mysql.connector.Error as error:
            return {"message": error}

    def get_all(self):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("SELECT * FROM colors")

            return database_cursor.fetchall()
        except mysql.connector.Error as error:
            return {"message": error}

    def get_by_name(self, color_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            # we should pass a tuple therefore the weird comma right after id
            database_cursor.execute("SELECT * FROM colors WHERE color_name = %s", (color_name,))

            color = database_cursor.fetchone()
            if database_cursor.rowcount == 0:
                return {"message": "No color found with that name"}
            else:
                return color
        except mysql.connector.Error as error:
            return {"message": error}

    def delete(self, color_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            # we should pass a tuple therefore the weird comma right after id
            database_cursor.execute("DELETE FROM colors WHERE color_name = %s", (color_name,))
            database_cursor.fetchone()

            database.commit()

            return {"message": "Color succesfully deleted"}
        except mysql.connector.Error as error:
            return {"message": error}

    def update(self, old_name: str, new_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()
            
            database_cursor.execute("UPDATE colors \
                                    SET color_name = %s \
                                    WHERE color_name = %s",
                                    (new_name, old_name))

            database.commit()

            if database_cursor.rowcount == 1:
                return {"message": "row succesfully updated!"}
            else:
                return {"message": "No color with that name found"}
        except mysql.connector.Error as error:
            return {"message": error}
