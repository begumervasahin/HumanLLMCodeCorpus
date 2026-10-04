import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.stats import skew
import numpy as np
import re
def fonk1():
    print('\n\n                 Welcome to SkewU.py')
    print('                 --by Niam Moltta--')
    print('                      ~~/\\
    print('\n\n\n')
    print('Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select b4.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n')
    b1 = input('Enter .csv file name: ')
    if not b1:
        print('\nArrivederci!\n')
        exit()
    print(' ')
    b2 = pd.read_csv(b1)
    b3 = b2.b3.to_numpy()
    while True:
        print(f'\nColumns in {re.findall("(.+?).csv", b1)} are:\n')
        print(b3)
        print(' ')
        b4 = input('Enter b4 header: ')
        if not b4 or b4.lower() == 'ya':
            break
        elif b4 in b3:
            b2[b4].fillna(0, b5 = True)
            print('Missing values replaced with zeros.\n')
            b6 = scale(b2[b4])
            b7 = skew(b6)
            print(f'b8 = {b7}')
            fonk2(b6, b4, b7)
        else:
            print('Invalid b4 name. Please try again.')
    print('\nHasta la vista, human.\n')
def fonk2(b2, b4, b7):
    plt.figure(b9 = (12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(b2, b10 = 'lightblue', alpha=0.75)
    plt.xlabel("b8 greater than zero shows large skewed distribution -->")
    plt.title(b4)
    plt.text(2, 100000, f"b8: {b7:.2f}")
    plt.subplot(1, 2, 2)
    plt.boxplot(b2)
    plt.title("Skewed Distribution")
    plt.xlabel(f"{b7:.2f}")
    plt.tight_layout()
    plt.show()
if b11 = = "__main__":
    fonk1()