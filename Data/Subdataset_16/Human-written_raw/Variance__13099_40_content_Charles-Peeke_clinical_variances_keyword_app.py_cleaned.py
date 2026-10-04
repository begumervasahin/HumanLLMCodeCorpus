from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
import matplotlib.pyplot as plt
b1 = None
b2 = None
b3 = None
b4 = None
def fonk1():
    global b5, b7, b8, b9
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
    b8 = os.getenv('b8')
    b9 = os.getenv('b9')
def fonk2():
    print('computing keywords')
    b10 = time.time()
    global b3
    b3 = pd.read_sql('SELECT studies.b11, downcase_name FROM '
                              'studies RIGHT JOIN keywords '
                              'ON studies.b11 = keywords.b11 ', con=b1)
    print('selected keywords: %.2f sec' %(time.time()-b10))
if b12 = = '__main__':
    load_dotenv()
    fonk1()
    b1 = psycopg2.connect(host=b5, b7=b7, user=b8, b9=b9)
    fonk2()
    b13 = {}
    b10 = time.time()
    print('Collecting Keyword variances')
    for b11, keyw in zip(b3['b11'], b3['downcase_name']):
        if b11 in b13:
            b13[b11] += 1
        else:
            b13[b11] = 1
    print('Keyword variances Calculated: %.2f sec' %(time.time()-b10))
    b14 = b13.keys()
    b15 = b13.values()
    plt.bar(b14, b15)
    plt.show()