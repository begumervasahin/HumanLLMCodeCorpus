import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.stats import skew
import numpy as np
import re
def display_welcome_message():
    print(" ")
    print(" ")
    print("                 Welcome to SkewU.py")
    print("                 --by Niam Moltta--")
    print("                      ~~/\
    print(" ")
    print(" ")
    print(" ")
    print("Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select column.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n")
def get_file_name():
    file_name = input('Enter .csv file name: ')
    if file_name == '':
        print(" ")
        print("Arrivederci!")
        print(" ")
        exit()
    return file_name
def load_data(file_name):
    return pd.read_csv(file_name)
def get_column_name(columns, file_name):
    print(" ")
    print(f"Columns in {re.findall('(.+?).csv', file_name)[0]} are:\n")
    print(columns)
    print(" ")
    column = input('Enter column header: ')
    return column
def process_column(data, column):
    data[column].fillna(0, inplace=True)
    print('Missing values replaced with zeros.')
    print(" ")
    scaled_col = scale(data[column])
    skewness_value = skew(scaled_col)
    print(f'Skewness = {skewness_value:.2f}')
    return scaled_col, skewness_value
def plot_data(column, scaled_col, skewness_value):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(scaled_col, facecolor='lightblue', alpha=0.75)
    axes[0].set_title(column)
    axes[0].set_xlabel("Skewness greater than zero shows large skewed distribution -->")
    axes[0].text(2, 100000, f"Skewness = {skewness_value:.2f}")
    axes[1].boxplot(scaled_col)
    axes[1].set_title("Skewed Distribution")
    axes[1].set_xlabel(f"Skewness = {skewness_value:.2f}")
    plt.show()
def main():
    display_welcome_message()
    file_name = get_file_name()
    data = load_data(file_name)
    columns = data.columns.to_numpy()
    while True:
        column = get_column_name(columns, file_name)
        if column == '' or column.lower() == 'ya':
            break
        if column in data.columns:
            scaled_col, skewness_value = process_column(data, column)
            plot_data(column, scaled_col, skewness_value)
        else:
            print(f"Column '{column}' not found. Please enter a valid column name.")
    print('\nHasta la vista, human.\n')
if __name__ == "__main__":
    main()