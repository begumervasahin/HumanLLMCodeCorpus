import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.stats import skew
import numpy as np
import re
def main():
    print('\n\n                 Welcome to SkewU.py')
    print('                 --by Niam Moltta--')
    print('                      ~~/\\
    print('\n\n\n')
    print('Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select column.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n')
    fhand = input('Enter .csv file name: ')
    if not fhand:
        print('\nArrivederci!\n')
        exit()
    print(' ')
    data = pd.read_csv(fhand)
    columns = data.columns.to_numpy()
    while True:
        print(f'\nColumns in {re.findall("(.+?).csv", fhand)} are:\n')
        print(columns)
        print(' ')
        column = input('Enter column header: ')
        if not column or column.lower() == 'ya':
            break
        elif column in columns:
            data[column].fillna(0, inplace=True)
            print('Missing values replaced with zeros.\n')
            col_scaled = scale(data[column])
            skness = skew(col_scaled)
            print(f'Skewness = {skness}')
            plot_skewness(col_scaled, column, skness)
        else:
            print('Invalid column name. Please try again.')
    print('\nHasta la vista, human.\n')
def plot_skewness(data, column, skness):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(data, facecolor='lightblue', alpha=0.75)
    plt.xlabel("Skewness greater than zero shows large skewed distribution -->")
    plt.title(column)
    plt.text(2, 100000, f"Skewness: {skness:.2f}")
    plt.subplot(1, 2, 2)
    plt.boxplot(data)
    plt.title("Skewed Distribution")
    plt.xlabel(f"{skness:.2f}")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()