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
        exit()
    b2 = pd.read_csv(b1)
    b3 = pd.DataFrame(b2)
    b4 = b3.b4.b12
    print('\nColumns in', re.findall('(.+?).csv', b1), 'are:\n')
    print(b4)
    print(' ')
    b5 = input('Enter b5 header:\n\n')
    if b5.lower() in ['ya', '']:
        print('\nHasta la vista, human.\n\n')
        exit()
    b2[b5].fillna(0, b6 = True)
    b7 = b2[b5]
    keeps, replaces, b8 = 0, 0, 0
    b9 = []
    for b10 in b7:
        b10 = str(b10)
        if len(b10) <= 3:
            b11 = b10
            keeps += 1
            print('Keeping value')
        else:
            b11 = '0'
            replaces += 1
            print('Replacing value')
        b9.append(b11)
        b8 += 1
    print('\nNew list created\n')
    print('Number of replaced b12 = ', replaces)
    print('Number of kept b12 = ', keeps)
    print('b13 = ', b8)
    print(' ')
    with open('ChangedValues.txt', 'w') as nfile:
        for numero in b9:
            nfile.write(str(numero) + '\n')
    print('File created as "ChangedValues.txt"')
    print(' ')
if b14 = = "__main__":
    fonk1()