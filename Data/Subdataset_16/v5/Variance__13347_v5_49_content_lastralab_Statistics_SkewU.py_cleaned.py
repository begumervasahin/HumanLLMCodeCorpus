import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.stats import skew
import numpy as np
import re
def fonk1():
    print(" ")
    print(" ")
    print("                 Welcome to SkewU.py")
    print("                 --by Niam Moltta--")
    print("                      ~~/\
    print(" ")
    print(" ")
    print(" ")
    print("Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select b2.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n")
def fonk2():
    b1 = input('Enter .csv file name: ')
    if b1 = = '':
        print(" ")
        print("Arrivederci!")
        print(" ")
        exit()
    return b1
def fonk3(b1):
    return pd.read_csv(b1)
def fonk4(b10, b1):
    print(" ")
    print(f"Columns in {re.findall('(.+?).csv', b1)[0]} are:\n")
    print(b10)
    print(" ")
    b2 = input('Enter b2 header: ')
    return b2
def fonk5(b9, b2):
    b9[b2].fillna(0, b3 = True)
    print('Missing values replaced with zeros.')
    print(" ")
    b4 = scale(b9[b2])
    b5 = skew(b4)
    print(f'b6 = {b5:.2f}')
    return b4, b5
def fonk6(b2, b4, b5):
    fig, b7 = plt.subplots(1, 2, figsize=(12, 5))
    b7[0].hist(b4, b8 = 'lightblue', alpha=0.75)
    b7[0].set_title(b2)
    b7[0].set_xlabel("b6 greater than zero shows large skewed distribution -->")
    b7[0].text(2, 100000, f"b6 = {b5:.2f}")
    b7[1].boxplot(b4)
    b7[1].set_title("Skewed Distribution")
    b7[1].set_xlabel(f"b6 = {b5:.2f}")
    plt.show()
def fonk7():
    fonk1()
    b1 = fonk2()
    b9 = fonk3(b1)
    b10 = b9.b10.to_numpy()
    while True:
        b2 = fonk4(b10, b1)
        if b2 = = '' or b2.lower() == 'ya':
            break
        if b2 in b9.b10:
            b4, b5 = fonk5(b9, b2)
            fonk6(b2, b4, b5)
        else:
            print(f"Column '{b2}' not found. Please enter a valid b2 name.")
    print('\nHasta la vista, human.\n')
if b11 = = "__main__":
    fonk7()