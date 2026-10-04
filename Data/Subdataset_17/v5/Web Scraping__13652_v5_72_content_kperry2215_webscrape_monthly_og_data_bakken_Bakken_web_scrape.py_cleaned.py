import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def fetch_and_process_data(url, file_path):
    response = requests.get(url)
    workbook = xlrd.open_workbook(file_contents=response.content)
    worksheet = workbook.sheet_by_index(0)
    datemode = workbook.datemode
    for i in range(1, worksheet.nrows):
        cell_value = worksheet.cell_value(i, 0)
        year, month, day, _, _, _ = xlrd.xldate_as_tuple(cell_value, datemode)
        formatted_date = datetime(year, month, 1).strftime("%m/%Y")
        worksheet._cell_values[i][0] = formatted_date
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for rownum in range(worksheet.nrows):
            writer.writerow(worksheet.row_values(rownum))
    return pd.read_csv(file_path)
def pull_desired_files_and_create_master_df(dates, base_url, save_dir):
    master_df = pd.DataFrame()
    for date in dates:
        file_url = f"{base_url}{date}.xlsx"
        csv_file_path = os.path.join(save_dir, f"{date}.csv")
        data_df = fetch_and_process_data(file_url, csv_file_path)
        master_df = master_df.append(data_df, ignore_index=True)
    return master_df
def main():
    save_dir = r'C:\Bakken'
    base_url = "https:
    os.makedirs(save_dir, exist_ok=True)
    dates = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    master_df = pull_desired_files_and_create_master_df(dates, base_url, save_dir)
    master_df['ReportDate'] = pd.to_datetime(master_df['ReportDate'], format='%m/%Y')
    master_df.to_csv(os.path.join(save_dir, 'master_dataframe_production.csv'), index=False)
if __name__ == "__main__":
    main()