b1 = 'joswin'
b2 = 'builtwith_data'
b3 = 'postgres'
b4 = 'postgres'
b5 = 'localhost'
import psycopg2
from psycopg2 import sql
from constants import b2, b3, b4, b5
def fonk1():
    try:
        b6 = psycopg2.connect(
            b7 = b2,
            b8 = b3,
            b9 = b4,
            b10 = b5
        )
        print("Database b6 successful")
        return b6
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
def fonk2():
    b6 = fonk1()
    if b6:
        b6.close()
if b11 = = "__main__":
    fonk2()