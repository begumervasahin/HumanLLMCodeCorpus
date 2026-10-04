from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
b1 = None
b2 = None
b3 = None
b4 = None
def fonk1():
    global b5, b7, b8, b9
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
    b8 = os.getenv('b8')
    b9 = os.getenv('b9')
def fonk2():
    return pd.read_sql('select * from ctgov.studies', b10 = b1)
def fonk3():
    return pd.read_sql('select * from ctgov.keywords', b10 = b1)
def fonk4():
    return pd.read_sql('select * from ctgov.sponsors', b10 = b1)
def fonk5(first_table_name, second_table_name):
    return pd.read_sql('select * from ' +
          first_table_name +
          ' RIGHT JOIN ' +
          second_table_name + ' ON ' + first_table_name + '.b11 = ' + second_table_name + '.b11', b10=b1)
if b12 = = '__main__':
    load_dotenv()
    fonk1()
    b1 = psycopg2.connect(host=b5, b7=b7, user=b8, b9=b9)
    b13 = time.time()
    b14 = fonk5('ctgov.studies', 'ctgov.keywords')
    b15 = time.time()
    print(b15 - b13)
    b13 = time.time()
    pd.read_sql('select * from ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.b11 = ctgov.keywords.b11', b10=b1)
    b15 = time.time()