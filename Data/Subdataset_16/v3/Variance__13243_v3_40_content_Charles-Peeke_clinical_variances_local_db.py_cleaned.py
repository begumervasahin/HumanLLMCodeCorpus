from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
def fonk1():
    load_dotenv()
    global b1, b2, b3, b4, b5
    b1 = os.getenv('b1')
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
def fonk2():
    return psycopg2.connect(
        b6 = b1,
        b2 = b2,
        b3 = b3,
        b7 = b4,
        b5 = b5
    )
def fonk3(b14, table_name):
    b8 = f"SELECT * FROM {table_name}"
    return pd.read_sql(b8, b9 = b14)
def fonk4(b14, first_table_name, second_table_name):
    b8 = f
    return pd.read_sql(b8, b9 = b14)
def fonk5(func, *args):
    b10 = time.time()
    b11 = func(*args)
    b12 = time.time()
    return b11, b12 - b10
if b13 = = '__main__':
    fonk1()
    b14 = fonk2()
    joined_results, b15 = fonk5(join_tables, b14, 'ctgov.studies', 'ctgov.keywords')
    print("Join operation time using function:", b15)
    b8 = 'SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.nct_id = ctgov.keywords.nct_id'
    _, b16 = fonk5(pd.read_sql, b8, b14)
    print("Join operation time using raw SQL:", b16)
    b14.close()