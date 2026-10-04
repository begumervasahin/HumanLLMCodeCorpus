from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
import numpy as np
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
def fonk1():
    global b6, b8, b9, b10
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
    b8 = os.getenv('b8')
    b9 = os.getenv('b9')
    b10 = os.getenv('b10')
def fonk2():
    b2 = pd.read_sql('SELECT * FROM studies', con=b1)
    return b2
def fonk3():
    b2 = pd.read_sql('SELECT * FROM sponsors', con=b1)
    return b2
def fonk4():
    b3 = pd.read_sql('SELECT * FROM keywords', con=b1)
    return b3
def fonk5():
    b5 = pd.read_sql('SELECT * FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=b1)
    return b5
def fonk6():
    b4 = pd.read_sql('SELECT * FROM studies RIGHT JOIN keywords ON studies.nct_id = keywords.nct_id', con=b1)
    return b4
if b11 = = '__main__':
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    load_dotenv()
    fonk1()
    b1 = psycopg2.connect(host=b6, b8=b8, user=b9, b10=b10)
    b16 = time.time()
    b17 = fonk2()
    b18 = fonk4()
    b19 = pd.merge(b17, b18, how='right', on='nct_id')
    b20 = time.time()
    print(b20 - b16)
    print(b19)