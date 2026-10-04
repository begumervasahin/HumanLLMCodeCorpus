import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def pull_desired_files_and_create_master_df(dates):
    base_url = "https:
    master_df = pd.DataFrame()
    for date in dates:
        desired_url = f"{base_url}{date}.xlsx"
        response = requests.get(desired_url)
        workbook = xlrd.open_workbook(file_contents=response.content)
        worksheet = workbook.sheet_by_index(0)
        for i in range(1, worksheet.nrows):
            wrong_value = worksheet.cell_value(i, 0)
            workbook_datemode = workbook.datemode
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(wrong_value, workbook_datemode)
            worksheet._cell_values[i][0] = datetime(year, month, 1).strftime("%m/%Y")
        file_name = f'C:/Bakken/{date}.csv'
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for rownum in range(worksheet.nrows):
                writer.writerow(worksheet.row_values(rownum))
        dataframe = pd.read_csv(file_name)
        master_df = master_df.append(dataframe)
    return master_df
def main():
    newpath = r'C:\Bakken'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    dates = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    master_df = pull_desired_files_and_create_master_df(dates)
    master_df['ReportDate'] = pd.to_datetime(master_df['ReportDate'])
    master_df.to_csv(f'{newpath}/master_dataframe_production.csv', index=False)
if __name__ == "__main__":
    main()