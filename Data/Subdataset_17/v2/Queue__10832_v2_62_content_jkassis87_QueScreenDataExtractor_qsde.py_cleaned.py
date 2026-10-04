import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
def fetch_ticket_data(url, user, password):
    response = requests.get(url, auth=(user, password))
    response.raise_for_status()
    ticket_data = response.json()
    flattened_data = flatten(ticket_data)
    return list(flattened_data.values())
def authorize_google_sheets(credentials_file, scope):
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    return gspread.authorize(creds)
def update_google_sheet(client, ticket_values, template_file):
    now = datetime.now()
    daynow = now.day
    yearmonth = f"{now.year}-{now.month}"
    try:
        sheet = client.open(yearmonth)
    except gspread.SpreadsheetNotFound:
        sheet = client.create(yearmonth)
        sheet.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
    worksheet = sheet.add_worksheet(title=str(daynow), rows="17", cols="25")
    with open(template_file, 'r') as file:
        csv_template = file.read()
    client.import_csv(sheet.id, csv_template)
    row, col = 2, 2
    for index, value in enumerate(ticket_values):
        worksheet.update_cell(row, col, value)
        row += 1
        if (index + 1) % 11 == 0:
            row = 2
            col += 1
if __name__ == "__main__":
    TICKET_DATA_URL = 'http:
    USERNAME = 'X'
    PASSWORD = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    CREDENTIALS_FILE = 'client_secret.json'
    SCOPE = ['https:
    TEMPLATE_FILE = 'qsdetemplate.csv'
    try:
        ticket_values = fetch_ticket_data(TICKET_DATA_URL, USERNAME, PASSWORD)
        gsheet_client = authorize_google_sheets(CREDENTIALS_FILE, SCOPE)
        update_google_sheet(gsheet_client, ticket_values, TEMPLATE_FILE)
        print("Google Sheets update complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)