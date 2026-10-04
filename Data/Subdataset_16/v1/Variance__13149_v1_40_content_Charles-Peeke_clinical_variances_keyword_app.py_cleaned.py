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
    print(f'Keywords fetched in {time.time() - b8:.2f} seconds')
    return b11
def fonk4(b11):
    print('Calculating keyword variances...')
    b8 = time.time()
    b12 = {}
    for b10, keyw in zip(b11['b10'], b11['downcase_name']):
        if b10 in b12:
            b12[b10] += 1
        else:
            b12[b10] = 1
    print(f'Keyword variances calculated in {time.time() - b8:.2f} seconds')
    return b12
def fonk5(b12):
    b13 = list(b12.keys())
    b14 = list(b12.values())
    plt.figure(b15 = (10, 6))
    plt.bar(b13, b14)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances by NCT ID')
    plt.xticks(b16 = 90)
    plt.tight_layout()
    plt.show()
def fonk6():
    b1 = fonk1()
    b2 = fonk2(b1)
    b11 = fonk3(b2)
    b12 = fonk4(b11)
    fonk5(b12)
    b2.close()
if b17 = = '__main__':
    fonk6()