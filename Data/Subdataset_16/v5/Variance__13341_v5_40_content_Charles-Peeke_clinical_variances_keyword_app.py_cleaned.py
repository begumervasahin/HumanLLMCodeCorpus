import os
import time
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
b1 = None
b2 = None
def fonk1():
    global b3, b4, b5, b6, b7
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
def fonk2():
    print('Fetching keywords...')
    b8 = time.time()
    global b2
    b9 = '''
    SELECT studies.b10, downcase_name
    FROM studies
    RIGHT JOIN keywords
    ON studies.b10 = keywords.b10
    '''
    b2 = pd.read_sql(b9, con=b1)
    b11 = time.time() - b8
    print(f'Keywords fetched in {b11:.2f} seconds')
def fonk3():
    print('Calculating keyword variances...')
    b8 = time.time()
    b12 = b2['b10'].value_counts()
    b11 = time.time() - b8
    print(f'Keyword variances calculated in {b11:.2f} seconds')
    plt.bar(b12.index, b12.values)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances')
    plt.show()
def fonk4():
    load_dotenv()
    fonk1()
    global b1
    b1 = psycopg2.connect(
        b13 = b3,
        b4 = b4,
        b5 = b5,
        b14 = b6,
        b7 = b7
    )
    fonk2()
    fonk3()
if b15 = = '__main__':
    fonk4()