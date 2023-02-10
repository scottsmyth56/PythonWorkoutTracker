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
