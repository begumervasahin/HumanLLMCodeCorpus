import numpy as np
import pandas as pd
import re
def fonk1():
    print('\n' * 3)
    print('          Welcome to ConverS.py')
    print('           --by Niam Moltta--')
    print('                ~~/\
    print('\n' * 3)
    print('Application: STRINGS TO NUMBERS TRANSFORMATION.\n\nINSTRUCTIONS:\n\n-You need to modify the code itself in order to convert your own b8.\n\n')
def fonk2():
    b1 = input('File name: ')
    if not b1:
        print('\nArrivederci!\n')
        exit()
    return b1
def fonk3(b1):
    return pd.read_csv(b1)
def fonk4(b8, b1):
    print('\nColumns in', re.findall('(.+?).csv', b1)[0], 'are:\n')
    print(b8.columns.to_list())
    print(' ')
def fonk5(b8):
    b2 = input('Enter b2 header:\n\n')
    if not b2:
        print('\nHasta la vista, human.\n\n')
        exit()
    if b2 not in b8.columns:
        print(f"\nColumn '{b2}' not found in the b8.\n\n")
        exit()
    return b2
def fonk6(b8, b2):
    b8[b2].fillna(0, b3 = True)
    b4 = b8[b2]
    keeps, replaces, b5 = 0, 0, 0
    b6 = []
    for b7 in b4:
        b7 = str(b7)
        if len(b7) <= 3:
            b6.append(b7)
            keeps += 1
            print('Keeping value')
        else:
            b6.append(0)
            replaces += 1
            print('Replacing value')
        b5 += 1
    return b6, keeps, replaces, b5
def fonk7(b6):
    with open('ChangedValues.txt', 'w') as nfile:
        for numero in b6:
            nfile.write(f'{numero}\n')
    print('File created as "ChangedValues.txt"\n')
def fonk8():
    fonk1()
    b1 = fonk2()
    b8 = fonk3(b1)
    fonk4(b8, b1)
    b2 = fonk5(b8)
    b6, keeps, replaces, b5 = fonk6(b8, b2)
    print('\nNew list created\n')
    print(f'Number of replaced b9 = {replaces}')
    print(f'Number of kept b9 = {keeps}')
    print(f'b10 = {b5}\n')
    fonk7(b6)
if b11 = = "__main__":
    fonk8()