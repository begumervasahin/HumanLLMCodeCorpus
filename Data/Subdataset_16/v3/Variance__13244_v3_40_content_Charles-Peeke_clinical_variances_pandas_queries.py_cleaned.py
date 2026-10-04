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
def fonk3(table_name):
    b9 = f'SELECT * FROM {table_name}'
    return pd.read_sql(b9, b10 = b1)
def fonk4(df1, df2, key, b11 = 'right'):
    return pd.merge(df1, df2, b11 = b11, on=key)
def fonk5(func):
    def fonk6(*args, **kwargs):
        b12 = time.time()
        b13 = func(*args, **kwargs)
        b14 = time.time() - b12
        print(f"Time taken: {b14} seconds")
        return b13
    return wrapper
@measure_execution_time
def fonk7():
    load_dotenv()
    fonk1()
    fonk2()
    b15 = fonk3('studies')
    b16 = fonk3('keywords')
    b17 = fonk4(b15, b16, 'nct_id')
    print(b17)
if b18 = = '__main__':
    fonk7()