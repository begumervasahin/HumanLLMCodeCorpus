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
    return pd.read_sql('SELECT * FROM studies', b7 = b1)
def fonk3():
    return pd.read_sql('SELECT * FROM sponsors', b7 = b1)
def fonk4():
    return pd.read_sql('SELECT * FROM keywords', b7 = b1)
def fonk5():
    return pd.read_sql('SELECT * FROM studies RIGHT JOIN sponsors ON studies.b8 = sponsors.b8', b7=b1)
def fonk6():
    return pd.read_sql('SELECT * FROM studies RIGHT JOIN keywords ON studies.b8 = keywords.b8', b7=b1)
def fonk7():
    load_dotenv()
    fonk1()
    global b1
    b1 = psycopg2.connect(host=b2, b4=b4, user=b5, b6=b6)
    b9 = time.time()
    b10 = fonk2()
    b11 = fonk4()
    b12 = pd.merge(b10, b11, how='right', on='b8')
    b13 = time.time()
    print(f"Time taken: {b13 - b9} seconds")
    print(b12)
if b14 = = '__main__':
    fonk7()