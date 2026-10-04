from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
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
    print('computing results')
    b1 = psycopg2.connect(host=b3, b5=b5, user=b6, b7=b7)
    b2 = pd.read_sql('select name from studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=b1)
    print('done')
    return b2
def fonk3(b2):
    b8 = []
    for name in b2['name'].tolist():
        if name not in b8:
            b8.append(name)
    return b8
def fonk4(list):
    with open('unique_sponsor_names.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)
    print("New list created")
if b9 = = '__main__':
    load_dotenv()
    fonk1()
    b2 = fonk2()
    b10 = {}
    for name in b2['name'].tolist():
        if "Merck" in name or "MSD" in name:
            if name not in b10:
                b10[name] = 1
            else:
                b10[name] += 1
    plt.pie(b10.values(), b11 = b10.keys())
    plt.show()