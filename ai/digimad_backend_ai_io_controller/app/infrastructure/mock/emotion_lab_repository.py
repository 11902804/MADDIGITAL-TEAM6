import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv   # for python-dotenv method
load_dotenv()                    # for python-dotenv method


class EmotionLabRepository:
    # if you have trouble connecting with database check readme
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

            database_cursor.execute("SELECT * FROM emotion_color")

            emotionlab_dict = {}
            index = 0
            for emotion_color in database_cursor.fetchall():
                emotion_name, nth_color, color_name = emotion_color
                print(emotion_name, nth_color, color_name)
                database_cursor.execute("SELECT hex_value FROM colors \
                                        WHERE color_name = %s", (color_name,))

                hex_value = database_cursor.fetchone()[0]
                print(color_name, hex_value)
                emotionlab_dict[index] = {
                    "emotion_name": emotion_name,
                    "hex_value": hex_value,
                    "color_name": color_name,
                    "nth_color": nth_color
                }

                index += 1

            if len(emotionlab_dict) == 0:
                return None
            else:
                return emotionlab_dict
        except mysql.connector.Error as error:
            return {"message": error}

    def get_by_id(self, emotion_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("SELECT * FROM emotion_color \
                                     WHERE emotion_name = %s", (emotion_name,))

            emotionlab_dict = {}
            index = 0
            for emotion_color in database_cursor.fetchall():
                emotion_name, nth_color, color_name = emotion_color
                database_cursor.execute("SELECT hex_value FROM colors \
                                        WHERE color_name = %s", (color_name,))

                hex_value = database_cursor.fetchone()[0]
                print(color_name, hex_value)
                emotionlab_dict[index] = {
                    "emotion_name": emotion_name,
                    "hex_value": hex_value,
                    "color_name": color_name,
                    "nth_color": nth_color
                }

                index += 1

            if len(emotionlab_dict) == 0:
                return None
            else:
                return emotionlab_dict
        except mysql.connector.Error as error:
            return {"message": error}

    def update(self, emotion_name: str, nth_color: int, color_name: str):
        try:
            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("UPDATE emotion_color \
                                    SET color_name = %s \
                                    WHERE emotion_name = %s \
                                    AND nth_color = %s", (color_name, emotion_name,
                                                        nth_color))

            database.commit()

            if database_cursor.rowcount == 1:
                return {"message": "row succesfully updated!"}
            else:
                return {"message": "oops! something went wrong"}
        except mysql.connector.Error as error:
            return {"message": error}
