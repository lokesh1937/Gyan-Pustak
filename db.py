import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="your_password",
        database="gyan_pustak"
    )