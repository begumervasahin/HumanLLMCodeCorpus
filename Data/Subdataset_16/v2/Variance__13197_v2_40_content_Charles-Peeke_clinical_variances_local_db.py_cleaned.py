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
    return psycopg2.connect(b6 = b1, b2=b2, b3=b3, user=b4, b5=b5)
def fonk3(b10):
    return pd.read_sql('SELECT * FROM ctgov.studies', b7 = b10)
def fonk4(b10):
    return pd.read_sql('SELECT * FROM ctgov.keywords', b7 = b10)
def fonk5(b10):
    return pd.read_sql('SELECT * FROM ctgov.sponsors', b7 = b10)
def fonk6(b10, first_table_name, second_table_name):
    b8 = f
    return pd.read_sql(b8, b7 = b10)
if b9 = = '__main__':
    fonk1()
    b10 = fonk2()
    b11 = time.time()
    b12 = fonk6(b10, 'ctgov.studies', 'ctgov.keywords')
    b13 = time.time()
    print("Join operation time using function:", b13 - b11)
    b11 = time.time()
    pd.read_sql('SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.b14 = ctgov.keywords.b14', b7=b10)
    b13 = time.time()
    print("Join operation time using raw SQL:", b13 - b11)
    b10.close()