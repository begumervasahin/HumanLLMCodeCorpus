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
def fonk3(b1, b10):
    print('\nColumns in', re.findall('(.+?).csv', b1), 'are:\n')
    print(b10)
    print(' ')
def fonk4():
    b2 = input('Enter b2 header:\n\n')
    if b2.lower() in ['ya', '']:
        print('\nHasta la vista, human.\n\n')
        exit()
    return b2
def fonk5(b8, b2):
    b8[b2].fillna(0, b3 = True)
    b4 = b8[b2]
    keeps, replaces, b5 = 0, 0, 0
    b6 = []
    for value in b4:
        b7 = str(value)
        if len(b7) <= 3:
            b6.append(b7)
            keeps += 1
            print('Keeping value')
        else:
            b6.append('0')
            replaces += 1
            print('Replacing value')
        b5 += 1
    return b6, keeps, replaces, b5
def fonk6(b11):
    with open('ChangedValues.txt', 'w') as file:
        for value in b11:
            file.write(value + '\n')
    print('File created as "ChangedValues.txt"')
def fonk7():
    fonk1()
    b1 = fonk2()
    b8 = pd.read_csv(b1)
    b9 = pd.DataFrame(b8)
    b10 = b9.b10.b11
    fonk3(b1, b10)
    b2 = fonk4()
    b6, keeps, replaces, b5 = fonk5(b8, b2)
    print('\nNew list created\n')
    print(f'Number of replaced b11 = {replaces}')
    print(f'Number of kept b11 = {keeps}')
    print(f'b12 = {b5}')
    print(' ')
    fonk6(b6)
if b13 = = "__main__":
    fonk7()