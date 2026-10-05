import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
def fonk1():
    global b1, b2, b3, b4, b5
    b1 = os.getenv('b1')
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
def fonk2():
    print('Fetching results from the b3...')
    b6 = psycopg2.connect(host=b1, b3=b3, user=b4, b5=b5)
    b7 = pd.read_sql('SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=b6)
    print('Results fetched successfully.')
    return b7
def fonk3(b7):
    b8 = []
    for name in b7['name'].tolist():
        if name not in b8:
            b8.append(name)
    return b8
def fonk4(lst):
    with open('unique_sponsor_names.txt', 'w') as f:
        for item in lst:
            f.write("%s\n" % item)
    print("Unique sponsor names written to file.")
if b9 = = '__main__':
    load_dotenv()
    fonk1()
    b7 = fonk2()
    b10 = {}
    for name in b7['name'].tolist():
        if "Merck" in name or "MSD" in name:
            if name not in b10:
                b10[name] = 1
            else:
                b10[name] += 1
    plt.pie(b10.values(), b11 = b10.keys())
    plt.show()