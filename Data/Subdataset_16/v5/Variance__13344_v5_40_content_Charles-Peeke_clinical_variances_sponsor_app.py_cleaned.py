from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
def fonk1():
    load_dotenv()
    return {
        "hostname": os.getenv('hostname'),
        "b2": os.getenv('b2'),
        "b3": os.getenv('b3'),
        "username": os.getenv('username'),
        "b5": os.getenv('b5')
    }
def fonk2(b10):
    return psycopg2.connect(
        b1 = b10['hostname'],
        b2 = b10['b2'],
        b3 = b10['b3'],
        b4 = b10['username'],
        b5 = b10['b5']
    )
def fonk3(b11):
    b6 = return pd.read_sql(b6, con=b11)
def fonk4(b12):
    return b12['name'].drop_duplicates().tolist()
def fonk5(list_data, filename):
    with open(filename, 'w') as file:
        for item in list_data:
            file.write(f"{item}\n")
    print(f"New list created in {filename}")
def fonk6(b12):
    b7 = b12['name'].str.contains("Merck|MSD", case=False, na=False)
    b8 = b12[b7]['name'].value_counts()
    plt.pie(b8.values, b9 = b8.index, autopct='%1.1f%%')
    plt.title("Distribution of Merck-related Sponsor Names")
    plt.show()
def fonk7():
    b10 = fonk1()
    b11 = fonk2(b10)
    b12 = fonk3(b11)
    b11.close()
    b13 = fonk4(b12)
    fonk5(b13, 'b13.txt')
    fonk6(b12)
if b14 = = '__main__':
    fonk7()