import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import psycopg2
def fonk1():
    load_dotenv()
    return {
        'hostname': os.getenv('hostname'),
        'b2': os.getenv('b2'),
        'b3': os.getenv('b3'),
        'username': os.getenv('username'),
        'b5': os.getenv('b5')
    }
def fonk2(b15):
    return psycopg2.connect(
        b1 = b15['hostname'],
        b2 = b15['b2'],
        b3 = b15['b3'],
        b4 = b15['username'],
        b5 = b15['b5']
    )
def fonk3(conn):
    print('Fetching keywords...')
    b6 = time.time()
    b7 = '''
        SELECT studies.b8, downcase_name
        FROM studies
        RIGHT JOIN keywords ON studies.b8 = keywords.b8
    '''
    b9 = pd.read_sql(b7, con=conn)
    b10 = time.time() - b6
    print(f'Keywords fetched in {b10:.2f} seconds')
    return b9
def fonk4(b9):
    print('Calculating keyword variances...')
    b6 = time.time()
    b11 = {}
    for b8 in b9['b8']:
        b11[b8] = b11.get(b8, 0) + 1
    b10 = time.time() - b6
    print(f'Keyword variances calculated in {b10:.2f} seconds')
    return b11
def fonk5(b11):
    ids, b12 = zip(*b11.items())
    plt.figure(b13 = (10, 6))
    plt.bar(ids, b12)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances by NCT ID')
    plt.xticks(b14 = 90)
    plt.tight_layout()
    plt.show()
def fonk6():
    b15 = fonk1()
    with fonk2(b15) as conn:
        b9 = fonk3(conn)
        b11 = fonk4(b9)
        fonk5(b11)
if b16 = = '__main__':
    fonk6()