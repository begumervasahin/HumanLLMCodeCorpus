import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import psycopg2
def fonk1():
    load_dotenv()
    b1 = {
        'hostname': os.getenv('hostname'),
        'b4': os.getenv('b4'),
        'b5': os.getenv('b5'),
        'username': os.getenv('username'),
        'b7': os.getenv('b7')
    }
    return b1
def fonk2(b1):
    b2 = psycopg2.connect(
        b3 = b1['hostname'],
        b4 = b1['b4'],
        b5 = b1['b5'],
        b6 = b1['username'],
        b7 = b1['b7']
    )
    return b2
def fonk3(b2):
    print('Fetching keywords...')
    b8 = time.time()
    b9 = '''
        SELECT studies.b10, downcase_name
        FROM studies
        RIGHT JOIN keywords ON studies.b10 = keywords.b10
    '''
    b11 = pd.read_sql(b9, con=b2)
    b12 = time.time() - b8
    print(f'Keywords fetched in {b12:.2f} seconds')
    return b11
def fonk4(b11):
    print('Calculating keyword variances...')
    b8 = time.time()
    b13 = {}
    for b10, keyw in zip(b11['b10'], b11['downcase_name']):
        if b10 in b13:
            b13[b10] += 1
        else:
            b13[b10] = 1
    b12 = time.time() - b8
    print(f'Keyword variances calculated in {b12:.2f} seconds')
    return b13
def fonk5(b13):
    b14 = list(b13.keys())
    b15 = list(b13.values())
    plt.figure(b16 = (10, 6))
    plt.bar(b14, b15)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances by NCT ID')
    plt.xticks(b17 = 90)
    plt.tight_layout()
    plt.show()
def fonk6():
    b1 = fonk1()
    b2 = fonk2(b1)
    b11 = fonk3(b2)
    b13 = fonk4(b11)
    fonk5(b13)
    b2.close()
if b18 = = '__main__':
    fonk6()