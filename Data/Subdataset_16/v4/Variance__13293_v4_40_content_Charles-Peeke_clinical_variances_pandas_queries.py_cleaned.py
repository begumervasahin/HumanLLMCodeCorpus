import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
b1 = None
def fonk1():
    load_dotenv()
    global b2, b3, b4, b5, b6
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
def fonk2():
    return psycopg2.connect(
        b7 = b2,
        b3 = b3,
        b4 = b4,
        b8 = b5,
        b6 = b6
    )
def fonk3(b10):
    return pd.read_sql(b10, b9 = b1)
def fonk4():
    return fonk3('SELECT * FROM studies')
def fonk5():
    return fonk3('SELECT * FROM sponsors')
def fonk6():
    return fonk3('SELECT * FROM keywords')
def fonk7():
    b10 = return fonk3(b10)
def fonk8():
    b10 = return fonk3(b10)
if b11 = = '__main__':
    fonk1()
    b1 = fonk2()
    b12 = time.time()
    b13 = fonk4()
    b14 = fonk6()
    b15 = pd.merge(b13, b14, how='right', on='nct_id')
    b16 = time.time()
    print("Time taken:", b16 - b12)
    print(b15)