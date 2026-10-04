import numpy as np
import pandas as pd
import re
def welcome_message():
    print('\n' * 3)
    print('          Welcome to ConverS.py')
    print('           --by Niam Moltta--')
    print('                ~~/\
    print('\n' * 3)
    print('Application: STRINGS TO NUMBERS TRANSFORMATION.\n\nINSTRUCTIONS:\n\n-You need to modify the code itself in order to convert your own data.\n\n')
def get_file_name():
    filecsv = input('File name: ')
    if not filecsv:
        print('\nArrivederci!\n')
        exit()
    return filecsv
def display_columns(filecsv, columns):
    print('\nColumns in', re.findall('(.+?).csv', filecsv), 'are:\n')
    print(columns)
    print(' ')
def get_column_name():
    column = input('Enter column header:\n\n')
    if column.lower() in ['ya', '']:
        print('\nHasta la vista, human.\n\n')
        exit()
    return column
def transform_column(data, column):
    data[column].fillna(0, inplace=True)
    numbers = data[column]
    keeps, replaces, total = 0, 0, 0
    transformed_values = []
    for value in numbers:
        value_str = str(value)
        if len(value_str) <= 3:
            transformed_values.append(value_str)
            keeps += 1
            print('Keeping value')
        else:
            transformed_values.append('0')
            replaces += 1
            print('Replacing value')
        total += 1
    return transformed_values, keeps, replaces, total
def save_transformed_values(values):
    with open('ChangedValues.txt', 'w') as file:
        for value in values:
            file.write(value + '\n')
    print('File created as "ChangedValues.txt"')
def main():
    welcome_message()
    filecsv = get_file_name()
    data = pd.read_csv(filecsv)
    frame = pd.DataFrame(data)
    columns = frame.columns.values
    display_columns(filecsv, columns)
    column = get_column_name()
    transformed_values, keeps, replaces, total = transform_column(data, column)
    print('\nNew list created\n')
    print(f'Number of replaced values = {replaces}')
    print(f'Number of kept values = {keeps}')
    print(f'Total = {total}')
    print(' ')
    save_transformed_values(transformed_values)
if __name__ == "__main__":
    main()