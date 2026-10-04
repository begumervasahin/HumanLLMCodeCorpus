import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()
b1 = os.getenv('b1')
b2 = os.getenv('b2')
b3 = os.getenv('b3')
b4 = os.getenv('b4')
b5 = os.getenv('b5')
def fonk1():
    print('Computing results...')
    b6 = psycopg2.connect(
        b7 = b1,
        b3 = b3,
        b8 = b4,
        b5 = b5
    )
    b9 = pd.read_sql(
        'SELECT name FROM studies RIGHT JOIN sponsors ON studies.b10 = sponsors.b10',
        b11 = b6
    )
    b6.close()
    print('Done')
    return b9
def fonk2(b9):
    return list(b9['name'].unique())
def fonk3(lst, b12 = 'unique_sponsor_names.txt'):
    with open(b12, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")
    print("New list created")
def fonk4(b9):
    b13 = {}
    for name in b9['name']:
        if "Merck" in name or "MSD" in name:
            if name not in b13:
                b13[name] = 1
            else:
                b13[name] += 1
    plt.pie(b13.values(), b14 = b13.keys(), autopct='%1.1f%%')
    plt.title('Distribution of Merck and MSD Sponsor Names')
    plt.show()
if b15 = = '__main__':
    b9 = fonk1()
    b16 = fonk2(b9)
    fonk3(b16)
    fonk4(b9)