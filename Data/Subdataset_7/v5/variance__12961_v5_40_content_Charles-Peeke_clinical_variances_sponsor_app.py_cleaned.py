import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
b1 = None
b2 = None
load_dotenv()
def fonk1():
    global b3, b4, b5, b6, b7
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
    b6 = os.getenv('b6')
    b7 = os.getenv('b7')
def fonk2():
    print('Computing results...')
    b1 = psycopg2.connect(host=b3, b5=b5, user=b6, b7=b7)
    b2 = pd.read_sql('SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=b1)
    print('Done.')
    return b2
def fonk3(b2):
    b8 = set(b2['name'].tolist())
    return list(b8)
def fonk4(names_list):
    with open('unique_sponsor_names.txt', 'w') as f:
        for name in names_list:
            f.write(f"{name}\n")
    print("New list created.")
if b9 = = '__main__':
    fonk1()
    b2 = fonk2()
    b10 = {name: b2['name'].tolist().count(name) for name in b2['name'].tolist() if "Merck" in name or "MSD" in name}
    plt.pie(b10.values(), b11 = b10.keys())
    plt.show()