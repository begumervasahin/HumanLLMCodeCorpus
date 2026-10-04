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
    print('Computing keywords...')
    b8 = time.time()
    global b2
    b9 = '''
    SELECT studies.b10, downcase_name
    FROM studies
    RIGHT JOIN keywords
    ON studies.b10 = keywords.b10
    '''
    b2 = pd.read_sql(b9, con=b1)
    print(f'Selected keywords: {time.time() - b8:.2f} sec')
def fonk3():
    print('Collecting Keyword variances...')
    b8 = time.time()
    b11 = {}
    for b10, keyword in zip(b2['b10'], b2['downcase_name']):
        b11[b10] = b11.get(b10, 0) + 1
    print(f'Keyword variances Calculated: {time.time() - b8:.2f} sec')
    b12 = b11.keys()
    b13 = b11.values()
    plt.bar(b12, b13)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances')
    plt.show()
if b14 = = '__main__':
    load_dotenv()
    fonk1()
    b1 = psycopg2.connect(host=b3, b5=b5, user=b6, b7=b7)
    fonk2()
    fonk3()