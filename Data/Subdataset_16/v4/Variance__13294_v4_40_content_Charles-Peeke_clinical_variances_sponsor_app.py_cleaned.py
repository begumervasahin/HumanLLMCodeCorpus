from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
def fonk1():
    load_dotenv()
    return {
        "hostname": os.getenv('hostname'),
        "port": os.getenv('port'),
        "b2": os.getenv('b2'),
        "username": os.getenv('username'),
        "b4": os.getenv('b4')
    }
def fonk2(b9):
    return psycopg2.connect(
        b1 = b9['hostname'],
        b2 = b9['b2'],
        b3 = b9['username'],
        b4 = b9['b4']
    )
def fonk3(b10):
    b5 = return pd.read_sql(b5, con=b10)
def fonk4(b11):
    return b11['name'].drop_duplicates().tolist()
def fonk5(list_data, filename):
    with open(filename, 'w') as file:
        for item in list_data:
            file.write(f"{item}\n")
    print(f"New list created in {filename}")
def fonk6(b11):
    b6 = b11['name'].str.contains("Merck|MSD", case=False, na=False)
    b7 = b11[b6]['name'].value_counts()
    plt.pie(b7.values, b8 = b7.index, autopct='%1.1f%%')
    plt.title("Distribution of Merck-related Sponsor Names")
    plt.show()
def fonk7():
    b9 = fonk1()
    b10 = fonk2(b9)
    b11 = fonk3(b10)
    b10.close()
    b12 = fonk4(b11)
    fonk5(b12, 'b12.txt')
    fonk6(b11)
if b13 = = '__main__':
    fonk7()