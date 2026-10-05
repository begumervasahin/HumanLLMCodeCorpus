import os
import time
import pandas as pd
import psycopg2
from dotenv import load_dotenv
b1 = None
b2 = None
b3 = None
b4 = None
def fonk1():
    global b5, b6, b7, b8, b9
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
    b8 = os.getenv('b8')
    b9 = os.getenv('b9')
def fonk2():
    global b1
    b1 = psycopg2.connect(host=b5, b7=b7, user=b8, b9=b9)
def fonk3(b11):
    return pd.read_sql(b11, b10 = b1)
def fonk4():
    b11 = 'SELECT * FROM ctgov.studies'
    return fonk3(b11)
def fonk5():
    b11 = 'SELECT * FROM ctgov.keywords'
    return fonk3(b11)
def fonk6():
    b11 = 'SELECT * FROM ctgov.sponsors'
    return fonk3(b11)
def fonk7(first_table_name, second_table_name):
    b11 = f
    return fonk3(b11)
if b12 = = '__main__':
    load_dotenv()
    fonk1()
    fonk2()
    b13 = time.time()
    b14 = fonk7('ctgov.studies', 'ctgov.keywords')
    b15 = time.time()
    print("Time taken for joining tables:", b15 - b13)
    b13 = time.time()
    b11 = fonk3(b11)
    b15 = time.time()
    print("Time taken for another b11:", b15 - b13)