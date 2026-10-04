import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fonk1(date, b18, b12):
    b1 = f"{b18}{date}.xlsx"
    b2 = requests.get(b1)
    with open(b12, 'wb') as temp_file:
        temp_file.write(b2.content)
def fonk2(b12, b14):
    b3 = xlrd.open_workbook(b12)
    b4 = b3.sheet_by_index(0)
    for i in range(1, b4.nrows):
        b5 = b4.b5(i, 0)
        year, month, *b6 = xlrd.xldate_as_tuple(b5, b3.datemode)
        b7 = datetime(year, month, 1).strftime("%m/%Y")
        b4._cell_values[i][0] = b7
    with open(b14, 'w', b8 = '') as csv_file:
        b9 = csv.b9(csv_file)
        for row_num in range(b4.nrows):
            b9.writerow(b4.row_values(row_num))
def fonk3(b14, b13):
    b10 = pd.read_csv(b14)
    return b13.append(b10, b11 = True)
def fonk4(b17, b18, b15):
    b12 = 'temp.xlsx'
    b13 = pd.DataFrame()
    for date in b17:
        b14 = os.path.join(b15, f"{date}.csv")
        fonk1(date, b18, b12)
        fonk2(b12, b14)
        b13 = fonk3(b14, b13)
    return b13
def fonk5():
    b15 = r'C:\Bakken'
    os.makedirs(b15, b16 = True)
    b17 = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    b18 = "https:
    b19 = fonk4(b17, b18, b15)
    b19['ReportDate'] = pd.to_datetime(b19['ReportDate'])
    b20 = os.path.join(b15, 'b19.csv')
    b19.to_csv(b20, b21 = False)
if b22 = = "__main__":
    fonk5()