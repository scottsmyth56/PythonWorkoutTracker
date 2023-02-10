import json
import mysql.connector

with open("creds.json", "r") as f:
    creds = json.load(f)

HOST = creds["HOST"]
USER = creds["USER"]
PASSWORD = creds["PASSWORD"]
PORT = creds["PORT"]
DATABASE = creds["NAME"]

conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    port=PORT,
    database=DATABASE
    )
cursor = conn.cursor()


def register_user(username, password):

    """
    Registers new user on the system with username and password
    If user already exists, messages is displayed,
    If user doesn't exist, the user is registered on the system
    """

    cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        print("User already Exists Please Try a Different Username")
        #add call to input function here
    else:
        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()



def _main_():