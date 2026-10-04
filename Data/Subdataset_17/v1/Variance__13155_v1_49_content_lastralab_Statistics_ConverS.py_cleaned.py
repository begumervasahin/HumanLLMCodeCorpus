import numpy as np
import pandas as pd
import re
def main():
    print('\n' * 3)
    print('          Welcome to ConverS.py')
    print('           --by Niam Moltta--')
    print('                ~~/\
    print('\n' * 3)
    print('Application: STRINGS TO NUMBERS TRANSFORMATION.\n\nINSTRUCTIONS:\n\n-You need to modify the code itself in order to convert your own data.\n\n')
    filecsv = input('File name: ')
    if not filecsv:
        print('\nArrivederci!\n')
        return
    data = pd.read_csv(filecsv)
    print('\nColumns in', re.findall('(.+?).csv', filecsv)[0], 'are:\n')
    print(data.columns.to_list())
    print(' ')
    column = input('Enter column header:\n\n')
    if not column:
        print('\nHasta la vista, human.\n\n')
        return
    if column not in data.columns:
        print(f"\nColumn '{column}' not found in the data.\n\n")
        return
    data[column].fillna(0, inplace=True)
    numbers = data[column]
    keeps, replaces, total = 0, 0, 0
    numeros = []
    for line in numbers:
        line = str(line)
        if len(line) <= 3:
            numeros.append(line)
            keeps += 1
            print('Keeping value')
        else:
            numeros.append(0)
            replaces += 1
            print('Replacing value')
        total += 1
    print('\nNew list created\n')
    print(f'Number of replaced values = {replaces}')
    print(f'Number of kept values = {keeps}')
    print(f'Total = {total}\n')
    with open('ChangedValues.txt', 'w') as nfile:
        for numero in numeros:
            nfile.write(f'{numero}\n')
    print('File created as "ChangedValues.txt"\n')
if __name__ == "__main__":
    main()