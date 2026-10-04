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
    try:
        b6 = psycopg2.connect(
            b7 = b1,
            b2 = b2,
            b3 = b3,
            b8 = b4,
            b5 = b5
        )
        b9 = 'SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id'
        b10 = pd.read_sql(b9, con=b6)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        b6.close()
    print('Done')
    return b10
def fonk2(b10):
    return b10['name'].unique().tolist()
def fonk3(lst, b11 = 'unique_sponsor_names.txt'):
    with open(b11, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")
    print("New list created")
def fonk4(b10):
    b12 = {}
    for name in b10['name']:
        if "Merck" in name or "MSD" in name:
            b12[name] = b12.get(name, 0) + 1
    plt.pie(b12.values(), b13 = b12.keys(), autopct='%1.1f%%')
    plt.title('Distribution of Merck and MSD Sponsor Names')
    plt.show()
if b14 = = '__main__':
    b10 = fonk1()
    b15 = fonk2(b10)
    fonk3(b15)
    fonk4(b10)