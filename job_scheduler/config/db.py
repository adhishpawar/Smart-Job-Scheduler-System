import mysql.connector

def __init__():
    pass

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="adhish@mysql",
        database="job_scheduler"
    )

conn = get_connection()
