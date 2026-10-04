__author__ = 'joswin'
DATABASE = 'builtwith_data'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
import psycopg2
from psycopg2 import sql
from constants import DATABASE, USER, PASSWORD, HOST
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
def main():
    connection = connect_to_database()
    if connection:
        connection.close()
if __name__ == "__main__":
    main()