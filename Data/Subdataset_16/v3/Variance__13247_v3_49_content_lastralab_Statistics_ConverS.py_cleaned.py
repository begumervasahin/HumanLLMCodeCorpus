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
def fonk2():
    b1 = input('File name: ')
    if not b1:
        print('\nArrivederci!\n')
        exit()
    return b1
def fonk3(b1):
    try:
        b2 = pd.read_csv(b1)
        return b2
    except FileNotFoundError:
        print(f"Error: File '{b1}' not found.")
        exit()
def fonk4(b2, b1):
    b3 = re.findall('(.+?).csv', b1)[0]
    print(f'\nColumns in {b3} are:\n')
    print(b2.columns.to_list())
    print(' ')
def fonk5(b2):
    b4 = input('Enter b4 header:\n\n')
    if not b4:
        print('\nHasta la vista, human.\n\n')
        exit()
    if b4 not in b2.columns:
        print(f"\nError: Column '{b4}' not found in the b2.\n\n")
        exit()
    return b4
def fonk6(b2, b4):
    b2[b4].fillna(0, b5 = True)
    b6 = b2[b4]
    keeps, replaces, b7 = 0, 0, 0
    b8 = []
    for value in b6:
        b9 = str(value)
        if len(b9) <= 3:
            b8.append(b9)
            keeps += 1
            print('Keeping value')
        else:
            b8.append(0)
            replaces += 1
            print('Replacing value')
        b7 += 1
    return b8, keeps, replaces, b7
def fonk7(b8):
    with open('ChangedValues.txt', 'w') as nfile:
        for value in b8:
            nfile.write(f'{value}\n')
    print('File created as "ChangedValues.txt"\n')
def fonk8():
    fonk1()
    b1 = fonk2()
    b2 = fonk3(b1)
    fonk4(b2, b1)
    b4 = fonk5(b2)
    b8, keeps, replaces, b7 = fonk6(b2, b4)
    print('\nNew list created\n')
    print(f'Number of replaced b10 = {replaces}')
    print(f'Number of kept b10 = {keeps}')
    print(f'b11 = {b7}\n')
    fonk7(b8)
if b12 = = "__main__":
    fonk8()