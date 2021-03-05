import os
import mysql.connector
import hashlib
from app.domain.models.authentication_error import AuthenticationError
from dotenv import load_dotenv   # for python-dotenv method
load_dotenv()                    # for python-dotenv method


class AuthRepository:
    def connect_to_database(self):
        # os environments are defined in .env file
                return mysql.connector.connect(host=os.environ.get('HOST'),
                                       user=os.environ.get('USER'),
                                       password=os.environ.get('PASSWORD'),
                                       database=os.environ.get('DATABASE'))

    def login(self, email: str, password: str):
            database = self.connect_to_database()
            database_cursor = database.cursor()

            database_cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            users = database_cursor.fetchall()

            # No user found with this email address
            if len(users) == 0:
                raise AuthenticationError('The email address {} does not exist in the database.'.format(email))

            # User found with this email address
            else:
                db_name = users[0][1]
                db_email = users[0][2]
                db_password = users[0][3]
                
                # Checking if password is correct
                password = hashlib.md5(str.encode(password)).hexdigest()
                if password == db_password:
                    return True, db_name
                else:
                    raise AuthenticationError('The entered password appears to be wrong.')
