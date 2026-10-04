import numpy as np
import pandas as pd
import re
def fonk1():
    print('\n' * 3)
    print('          Welcome to ConverS.py')
    print('           --by Niam Moltta--')
    print('                ~~/\
    print('\n' * 3)
    print('Application: STRINGS TO NUMBERS TRANSFORMATION.\n\nINSTRUCTIONS:\n\n-You need to modify the code itself in order to convert your own b2.\n\n')
    b1 = input('File name: ')
    if not b1:
        print('\nArrivederci!\n')
        return
    b2 = pd.read_csv(b1)
    print('\nColumns in', re.findall('(.+?).csv', b1)[0], 'are:\n')
    print(b2.columns.to_list())
    print(' ')
    b3 = input('Enter b3 header:\n\n')
    if not b3:
        print('\nHasta la vista, human.\n\n')
        return
    if b3 not in b2.columns:
        print(f"\nColumn '{b3}' not found in the b2.\n\n")
        return
    b2[b3].fillna(0, b4 = True)
    b5 = b2[b3]
    keeps, replaces, b6 = 0, 0, 0
    b7 = []
    for b8 in b5:
        b8 = str(b8)
        if len(b8) <= 3:
            b7.append(b8)
            keeps += 1
            print('Keeping value')
        else:
            b7.append(0)
            replaces += 1
            print('Replacing value')
        b6 += 1
    print('\nNew list created\n')
    print(f'Number of replaced b9 = {replaces}')
    print(f'Number of kept b9 = {keeps}')
    print(f'b10 = {b6}\n')
    with open('ChangedValues.txt', 'w') as nfile:
        for numero in b7:
            nfile.write(f'{numero}\n')
    print('File created as "ChangedValues.txt"\n')
if b11 = = "__main__":
    fonk1()