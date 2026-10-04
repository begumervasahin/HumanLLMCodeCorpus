import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
def fonk1():
    load_dotenv()
    b1 = {
        'hostname': os.getenv('hostname'),
        'b3': os.getenv('b3'),
        'b4': os.getenv('b4'),
        'username': os.getenv('username'),
        'b6': os.getenv('b6')
    }
    return b1
def fonk2(b1):
    return psycopg2.connect(
        b2 = b1['hostname'],
        b3 = b1['b3'],
        b4 = b1['b4'],
        b5 = b1['username'],
        b6 = b1['b6']
    )
def fonk3(b8, b9):
    return pd.read_sql(b8, b7 = b9)
def fonk4(b9):
    return fonk3('SELECT * FROM studies', b9)
def fonk5(b9):
    return fonk3('SELECT * FROM sponsors', b9)
def fonk6(b9):
    return fonk3('SELECT * FROM keywords', b9)
def fonk7(b9):
    b8 = return fonk3(b8, b9)
def fonk8(b9):
    b8 = return fonk3(b8, b9)
def fonk9():
    b1 = fonk1()
    b9 = fonk2(b1)
    b10 = time.time()
    b11 = fonk4(b9)
    b12 = fonk6(b9)
    b13 = pd.merge(b11, b12, how='right', on='nct_id')
    b14 = time.time()
    print(f"Time taken: {b14 - b10} seconds")
    print(b13)
if b15 = = '__main__':
    fonk9()