import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fonk1(b16):
    b1 = "https:
    b2 = pd.DataFrame()
    for date in b16:
        b3 = b1 + date + '.xlsx'
        b4 = requests.get(b3)
        b5 = 'temp.xlsx'
        with open(b5, 'wb') as f:
            f.write(b4.content)
        b6 = xlrd.open_workbook(b5)
        b7 = b6.sheet_by_index(0)
        for i in range(1, b7.nrows):
            b8 = b7.cell_value(i, 0)
            b9 = b6.datemode
            year, month, day, hour, minute, b10 = xlrd.xldate_as_tuple(b8, b9)
            b7._cell_values[i][0] = datetime(year, month, 1).strftime("%m/%Y")
        b11 = 'C:/Bakken/' + date + '.csv'
        with open(b11, 'w', b12 = '') as csv_file:
            b13 = csv.writer(csv_file)
            for rownum in range(b7.nrows):
                b13.writerow(b7.row_values(rownum))
        b14 = pd.read_csv(b11)
        b2 = b2.append(b14, ignore_index=True)
    return b2
def fonk2():
    b15 = b4'C:\Bakken'
    if not os.path.exists(b15):
        os.makedirs(b15)
    b16 = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    b17 = fonk1(b16)
    b17['ReportDate'] = pd.to_datetime(b17['ReportDate'])
    b18 = os.path.join(b15, 'b17.csv')
    b17.to_csv(b18, b19 = False)
if b20 = = "__main__":
    fonk2()