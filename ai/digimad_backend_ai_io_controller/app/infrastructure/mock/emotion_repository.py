import os
import mysql.connector
from dotenv import load_dotenv   # for python-dotenv method
load_dotenv()                    # for python-dotenv method


class EmotionRepository:
    # if you have trouble connecting with databse check readme
    def connect_to_database(self):
        # os environments are defined in .env file
        return mysql.connector.connect(host=os.environ.get('HOST'),
                                       user=os.environ.get('USER'),
                                       password=os.environ.get('PASSWORD'),
                                       database=os.environ.get('DATABASE'))

    def get_all(self):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("SELECT * FROM emotions")

            emotion_dict = {}
            for emotion in database_cursor.fetchall():
                emotion_dict[emotion[0]] = {
                    "emotion_name": emotion[1]
                }

            return emotion_dict
        except mysql.connector.Error as error:
            return {"message": "There was an error with the database"}

    def get_by_id(self, emotion_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            # we should pass a tuple therefore the weird comma right after emotion_name
            database_cursor.execute("SELECT * FROM emotions WHERE emotion_name = %s", (emotion_name,))

            return database_cursor.fetchall()
        except mysql.connector.Error as error:
            return {"message": "There was an error with the database"}
