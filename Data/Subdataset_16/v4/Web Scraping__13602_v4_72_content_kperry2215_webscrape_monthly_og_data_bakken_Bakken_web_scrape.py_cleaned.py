import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fonk1(b15):
    b1 = "https:
    b2 = pd.DataFrame()
    for date in b15:
        b3 = f"{b1}{date}.xlsx"
        b4 = requests.get(b3)
        b5 = xlrd.open_workbook(file_contents=b4.content)
        b6 = b5.sheet_by_index(0)
        for i in range(1, b6.nrows):
            b7 = b6.cell_value(i, 0)
            b8 = b5.datemode
            year, month, day, hour, minute, b9 = xlrd.xldate_as_tuple(b7, b8)
            b6._cell_values[i][0] = datetime(year, month, 1).strftime("%m/%Y")
        b10 = f'C:/Bakken/{date}.csv'
        with open(b10, 'w', b11 = '') as csv_file:
            b12 = csv.b12(csv_file)
            for rownum in range(b6.nrows):
                b12.writerow(b6.row_values(rownum))
        b13 = pd.read_csv(b10)
        b2 = b2.append(b13)
    return b2
def fonk2():
    b14 = r'C:\Bakken'
    if not os.path.exists(b14):
        os.makedirs(b14)
    b15 = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    b2 = fonk1(b15)
    b2['ReportDate'] = pd.to_datetime(b2['ReportDate'])
    b2.to_csv(f'{b14}/master_dataframe_production.csv', b16 = False)
if b17 = = "__main__":
    fonk2()