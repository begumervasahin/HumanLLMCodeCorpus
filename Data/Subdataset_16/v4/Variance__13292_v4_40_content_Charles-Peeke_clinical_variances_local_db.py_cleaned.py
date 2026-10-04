import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
b1 = None
def fonk1():
    load_dotenv()
    return {
        "hostname": os.getenv('hostname'),
        "b3": os.getenv('b3'),
        "b4": os.getenv('b4'),
        "username": os.getenv('username'),
        "b6": os.getenv('b6')
    }
def fonk2(b10):
    return psycopg2.connect(
        b2 = b10["hostname"],
        b3 = b10["b3"],
        b4 = b10["b4"],
        b5 = b10["username"],
        b6 = b10["b6"]
    )
def fonk3(table_name):
    return pd.read_sql(f'SELECT * FROM {table_name}', b7 = b1)
def fonk4(table1, table2):
    b8 = f
    return pd.read_sql(b8, b7 = b1)
if b9 = = '__main__':
    b10 = fonk1()
    b1 = fonk2(b10)
    b11 = time.time()
    b12 = fonk4('ctgov.studies', 'ctgov.keywords')
    b13 = time.time()
    print(f"Join operation time: {b13 - b11} seconds")
    b11 = time.time()
    pd.read_sql(, b7 = b1)
    b13 = time.time()
    print(f"Raw SQL join b8 time: {b13 - b11} seconds")
    b1.close()