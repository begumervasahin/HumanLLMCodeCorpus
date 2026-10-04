import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.stats import skew
import numpy as np
import re
def fonk1():
    fonk2()
    b1 = input('Enter .csv file name: ')
    if not b1:
        print('\nArrivederci!\n')
        exit()
    b2 = pd.read_csv(b1)
    b3 = b2.b3.to_numpy()
    while True:
        fonk3(b1, b3)
        b4 = input('Enter b4 header: ')
        if not b4 or b4.lower() == 'ya':
            break
        if b4 in b3:
            fonk4(b2, b4)
        else:
            print('Invalid b4 name. Please try again.')
    print('\nHasta la vista, human.\n')
def fonk2():
    print('\n\n                 Welcome to SkewU.py')
    print('                 --by Niam Moltta--')
    print('                      ~~/\\
    print('\n\n\n')
    print('Application: SKEWNESS CALCULATION.\n')
    print('INSTRUCTIONS:\n')
    print('- Select file, select b4.')
    print('- Returns skewness value.')
    print('- Returns skewness representation graph.\n')
def fonk3(file_name, b3):
    b5 = re.findall(r'(.+?).csv', file_name)[0]
    print(f'\nColumns in {b5} are:\n')
    print(b3)
    print(' ')
def fonk4(b2, b4):
    b2[b4].fillna(0, b6 = True)
    print('Missing values replaced with zeros.\n')
    b7 = scale(b2[b4])
    b8 = skew(b7)
    print(f'b9 = {b8}')
    fonk5(b7, b4, b8)
def fonk5(b2, b4, b8):
    plt.figure(b10 = (12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(b2, b11 = 'lightblue', alpha=0.75)
    plt.xlabel("b9 greater than zero shows large skewed distribution -->")
    plt.title(b4)
    plt.text(2, 100000, f"b9: {b8:.2f}")
    plt.subplot(1, 2, 2)
    plt.boxplot(b2)
    plt.title("Skewed Distribution")
    plt.xlabel(f"{b8:.2f}")
    plt.tight_layout()
    plt.show()
if b12 = = "__main__":
    fonk1()