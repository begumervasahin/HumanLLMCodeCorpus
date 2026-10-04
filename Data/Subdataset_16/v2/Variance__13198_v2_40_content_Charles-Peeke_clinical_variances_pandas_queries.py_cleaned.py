from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
b1 = None
def fonk1():
    global b2, b3, b4, b5, b6
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
def fonk2():
    global b1
    b1 = psycopg2.connect(
        b7 = b2,
        b4 = b4,
        b8 = b5,
        b6 = b6
    )
def fonk3(query):
    return pd.read_sql(query, b9 = b1)
def fonk4():
    load_dotenv()
    fonk1()
    fonk2()
    b10 = time.time()
    b11 = fonk3('SELECT * FROM studies')
    b12 = fonk3('SELECT * FROM keywords')
    b13 = pd.merge(b11, b12, how='right', on='nct_id')
    b14 = time.time()
    b15 = b14 - b10
    print(f"Time taken: {b15} seconds")
    print(b13)
if b16 = = '__main__':
    fonk4()