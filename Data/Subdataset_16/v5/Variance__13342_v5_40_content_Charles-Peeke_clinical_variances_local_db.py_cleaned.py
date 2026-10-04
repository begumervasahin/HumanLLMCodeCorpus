import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
b1 = None
def fonk1():
    load_dotenv()
    b2 = {
        "hostname": os.getenv('hostname'),
        "b5": os.getenv('b5'),
        "b6": os.getenv('b6'),
        "username": os.getenv('username'),
        "b8": os.getenv('b8')
    }
    return b2
def fonk2(b2):
    b3 = psycopg2.connect(
        b4 = b2["hostname"],
        b5 = b2["b5"],
        b6 = b2["b6"],
        b7 = b2["username"],
        b8 = b2["b8"]
    )
    return b3
def fonk3(table_name):
    b9 = f'SELECT * FROM {table_name}'
    b10 = pd.read_sql(b9, con=b1)
    return b10
def fonk4(table1, table2):
    b9 = f
    b11 = pd.read_sql(b9, con=b1)
    return b11
def fonk5(query_function, *args):
    b12 = time.time()
    query_function(*args)
    b13 = time.time()
    return b13 - b12
def fonk6():
    b2 = fonk1()
    global b1
    b1 = fonk2(b2)
    b14 = fonk5(join_tables, 'ctgov.studies', 'ctgov.keywords')
    print(f"Join operation time: {b14:.4f} seconds")
    b15 = fonk5(pd.read_sql, , con=b1)
    print(f"Raw SQL join b9 time: {b15:.4f} seconds")
    b1.close()
if b16 = = '__main__':
    fonk6()