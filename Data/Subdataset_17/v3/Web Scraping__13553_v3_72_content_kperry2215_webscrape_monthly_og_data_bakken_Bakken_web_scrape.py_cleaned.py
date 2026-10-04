import requests
import xlrd
import csv
import pandas as pd
from datetime import datetime
import os
def download_xlsx_file(date, base_url, temp_xlsx_path):
    url = f"{base_url}{date}.xlsx"
    response = requests.get(url)
    with open(temp_xlsx_path, 'wb') as temp_file:
        temp_file.write(response.content)
def convert_xlsx_to_csv(temp_xlsx_path, csv_file_path):
    workbook = xlrd.open_workbook(temp_xlsx_path)
    worksheet = workbook.sheet_by_index(0)
    for i in range(1, worksheet.nrows):
        cell_value = worksheet.cell_value(i, 0)
        year, month, *_ = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
        corrected_date = datetime(year, month, 1).strftime("%m/%Y")
        worksheet._cell_values[i][0] = corrected_date
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row_num in range(worksheet.nrows):
            writer.writerow(worksheet.row_values(row_num))
def append_csv_to_master_df(csv_file_path, master_df):
    dataframe = pd.read_csv(csv_file_path)
    return master_df.append(dataframe, ignore_index=True)
def pull_desired_files_and_create_master_df(dates, base_url, output_directory):
    temp_xlsx_path = 'temp.xlsx'
    master_df = pd.DataFrame()
    for date in dates:
        csv_file_path = os.path.join(output_directory, f"{date}.csv")
        download_xlsx_file(date, base_url, temp_xlsx_path)
        convert_xlsx_to_csv(temp_xlsx_path, csv_file_path)
        master_df = append_csv_to_master_df(csv_file_path, master_df)
    return master_df
def main():
    output_directory = r'C:\Bakken'
    os.makedirs(output_directory, exist_ok=True)
    dates = [
        '2016_12', '2017_01', '2017_02', '2017_03', '2017_04', '2017_05', '2017_06',
        '2017_07', '2017_08', '2017_09', '2017_10', '2017_11', '2017_12',
        '2018_01', '2018_02', '2018_03', '2018_04', '2018_05', '2018_06',
        '2018_07', '2018_08', '2018_09', '2018_10', '2018_11', '2018_12', '2019_01'
    ]
    base_url = "https:
    master_dataframe_production = pull_desired_files_and_create_master_df(dates, base_url, output_directory)
    master_dataframe_production['ReportDate'] = pd.to_datetime(master_dataframe_production['ReportDate'])
    master_csv_path = os.path.join(output_directory, 'master_dataframe_production.csv')
    master_dataframe_production.to_csv(master_csv_path, index=False)
if __name__ == "__main__":
    main()