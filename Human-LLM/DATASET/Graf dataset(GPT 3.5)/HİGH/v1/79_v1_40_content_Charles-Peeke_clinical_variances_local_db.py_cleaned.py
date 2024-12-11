from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
b1 = None
def fonk1():
    global b2, b4, b5, b6
    load_dotenv()
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
def fonk2():
    global b1
    b1 = psycopg2.connect(host=b2, b4=b4, user=b5, b6=b6)
def fonk3():
    return pd.read_sql('SELECT * FROM ctgov.studies', b7 = b1)
def fonk4():
    return pd.read_sql('SELECT * FROM ctgov.keywords', b7 = b1)
def fonk5(first_table_name, second_table_name):
    return pd.read_sql(f'SELECT * FROM {first_table_name} RIGHT JOIN {second_table_name} ON {first_table_name}.b8 = {second_table_name}.b8', b7=b1)
if b9 = = '__main__':
    fonk1()
    fonk2()
    b10 = time.time()
    b11 = fonk5('ctgov.studies', 'ctgov.keywords')
    b12 = time.time()
    print("Time taken for joining tables:", b12 - b10)
    b10 = time.time()
    pd.read_sql('SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.b8 = ctgov.keywords.b8', b7=b1)
    b12 = time.time()
    print("Time taken for joining tables (direct query):", b12 - b10)