# db_connection.py

import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"  # Replace with your actual MySQL password
DB_NAME = "project"

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
