import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
def fetch_ticket_data(url, username, password):
    response = requests.get(url, auth=(username, password))
    ticket_data = json.loads(response.text)
    return flatten(ticket_data)
def initialize_google_sheet(credentials_file, template_file):
    scope = ['https:
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    now = datetime.now()
    day_now = now.day
    year_month = f"{now.year}-{now.month}"
    try:
        sheet = client.open(year_month)
    except gspread.exceptions.SpreadsheetNotFound:
        client.create(year_month)
        sheet = client.open(year_month)
        sheet.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
    worksheet = sheet.add_worksheet(title=str(day_now), rows="17", cols="25")
    with open(template_file, 'r') as file:
        csv_template = file.read()
    client.import_csv(sheet.id, csv_template)
    return sheet, worksheet
def update_google_sheet(worksheet, data):
    row = 2
    col = 2
    count = 0
    for item in data:
        worksheet.update_cell(row, col, item)
        count += 1
        row += 1
        if count == 11:
            row = 2
            col += 1
            count = 0
def main():
    ticket_data_url = 'http:
    username = 'X'
    password = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    ticket_data = fetch_ticket_data(ticket_data_url, username, password)
    ticket_values = [value for _, value in ticket_data.items()]
    credentials_file = 'client_secret.json'
    template_file = 'qsdetemplate.csv'
    sheet, worksheet = initialize_google_sheet(credentials_file, template_file)
    update_google_sheet(worksheet, ticket_values)
if __name__ == "__main__":
    main()
    sys.exit()