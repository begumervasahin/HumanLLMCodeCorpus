import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fonk1(url, file_path):
    b1 = requests.get(url)
    b2 = xlrd.open_workbook(file_contents=b1.content)
    b3 = b2.sheet_by_index(0)
    b4 = b2.b4
    for i in range(1, b3.nrows):
        b5 = b3.b5(i, 0)
        year, month, day, b6, b6, b6 = xlrd.xldate_as_tuple(b5, b4)
        b7 = datetime(year, month, 1).strftime("%m/%Y")
        b3._cell_values[i][0] = b7
    with open(file_path, 'w', b8 = '') as csv_file:
        b9 = csv.b9(csv_file)
        for rownum in range(b3.nrows):
            b9.writerow(b3.row_values(rownum))
    return pd.read_csv(file_path)
def fonk2(b17, b15, b14):
    b10 = pd.DataFrame()
    for date in b17:
        b11 = f"{b15}{date}.xlsx"
        b12 = os.path.join(b14, f"{date}.csv")
        b13 = fonk1(b11, b12)
        b10 = b10.append(b13, ignore_index=True)
    return b10
def fonk3():
    b14 = r'C:\Bakken'
    b15 = "https:
    os.makedirs(b14, b16 = True)
    b17 = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    b10 = fonk2(b17, b15, b14)
    b10['ReportDate'] = pd.to_datetime(b10['ReportDate'], b18 = '%m/%Y')
    b10.to_csv(os.path.join(b14, 'master_dataframe_production.csv'), b19 = False)
if b20 = = "__main__":
    fonk3()