
b1 = 'joswin'
import psycopg2
from psycopg2 import sql
from constants import DATABASE, USER, PASSWORD, HOST
def fonk1():
    try:
        b2 = psycopg2.connect(
            b3 = DATABASE,
            b4 = USER,
            b5 = PASSWORD,
            b6 = HOST
        )
        print("Database b2 successful")
        return b2
    except psycopg2.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        return None
def fonk2():
    b2 = fonk1()
    if b2:
        try:
            pass
        finally:
            b2.close()
            print("Database b2 closed")
if b7 = = "__main__":
    fonk2()