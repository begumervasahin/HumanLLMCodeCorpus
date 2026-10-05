import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
def fonk1():
    load_dotenv()
def fonk2():
    global b1, b2, b3, b4, b5
    b1 = os.getenv('b1')
    b2 = os.getenv('b2')
    b3 = os.getenv('b3')
    b4 = os.getenv('b4')
    b5 = os.getenv('b5')
def fonk3():
    print('Fetching results from the b3...')
    with psycopg2.connect(b6 = b1, b3=b3, user=b4, b5=b5) as conn:
        b7 = 'SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id'
        b8 = pd.read_sql(b7, con=conn)
    print('Results fetched successfully.')
    return b8
def fonk4(b8):
    b9 = b8['name'].unique().tolist()
    return b9
def fonk5(b9):
    with open('unique_sponsor_names.txt', 'w') as file:
        for name in b9:
            file.write(f"{name}\n")
    print("Unique sponsor names written to file.")
if b10 = = '__main__':
    fonk1()
    fonk2()
    b8 = fonk3()
    b11 = {name: b8['name'].tolist().count(name) for name in b8['name'].tolist() if "Merck" in name or "MSD" in name}
    plt.pie(b11.values(), b12 = b11.keys())
    plt.show()