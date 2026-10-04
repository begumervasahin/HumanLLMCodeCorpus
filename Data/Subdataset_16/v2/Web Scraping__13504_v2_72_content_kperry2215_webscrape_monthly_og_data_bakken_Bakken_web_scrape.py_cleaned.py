import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fonk1(b17):
    b1 = "https:
    b2 = pd.DataFrame()
    for date in b17:
        b3 = b1 + date + '.xlsx'
        b4 = requests.get(b3)
        b5 = 'temp.xlsx'
        with open(b5, 'wb') as temp_file:
            temp_file.write(b4.content)
        b6 = xlrd.open_workbook(b5)
        b7 = b6.sheet_by_index(0)
        for i in range(1, b7.nrows):
            b8 = b7.b8(i, 0)
            b9 = b6.datemode
            year, month, day, hour, minute, b10 = xlrd.xldate_as_tuple(b8, b9)
            b11 = datetime(year, month, 1).strftime("%m/%Y")
            b7._cell_values[i][0] = b11
        b12 = f'C:/Bakken/{date}.csv'
        with open(b12, 'w', b13 = '') as csv_file:
            b14 = csv.b14(csv_file)
            for row_num in range(b7.nrows):
                b14.writerow(b7.row_values(row_num))
        b15 = pd.read_csv(b12)
        b2 = b2.append(b15, ignore_index=True)
    return b2
def fonk2():
    b16 = r'C:\Bakken'
    if not os.path.exists(b16):
        os.makedirs(b16)
    b17 = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    b18 = fonk1(b17)
    b18['ReportDate'] = pd.to_datetime(b18['ReportDate'])
    b19 = os.path.join(b16, 'b18.csv')
    b18.to_csv(b19, b20 = False)
if b21 = = "__main__":
    fonk2()