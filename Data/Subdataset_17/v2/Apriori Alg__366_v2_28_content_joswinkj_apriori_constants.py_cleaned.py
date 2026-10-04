
__author__ = 'joswin'
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
    except psycopg2.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        return None
def main():
    connection = connect_to_database()
    if connection:
        try:
            pass
        finally:
            connection.close()
            print("Database connection closed")
if __name__ == "__main__":
    main()