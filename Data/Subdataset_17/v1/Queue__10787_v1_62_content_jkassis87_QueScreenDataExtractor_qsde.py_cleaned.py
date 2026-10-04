import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
def fetch_ticket_data(url, user, password):
    response = requests.get(url, auth=(user, password))
    ticket_data = json.loads(response.text)
    flattened_data = flatten(ticket_data)
    return list(flattened_data.values())
def authorize_google_sheets(credentials_file, scope):
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    return client
def update_google_sheet(client, ticket_values, template_file):
    now = datetime.now()
    daynow = now.day
    yearmonth = f"{now.year}-{now.month}"
    try:
        sh = client.open(yearmonth)
    except gspread.SpreadsheetNotFound:
        sh = client.create(yearmonth)
        sh.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
    sh.add_worksheet(title=str(daynow), rows="17", cols="25")
    with open(template_file, 'r') as file:
        csv_template = file.read()
    client.import_csv(sh.id, csv_template)
    worksheet = sh.worksheet(str(daynow))
    row = 2
    col = 2
    ticket_count = 0
    for value in ticket_values:
        if ticket_count < 11:
            worksheet.update_cell(row, col, value)
            row += 1
            ticket_count += 1
        else:
            row = 2
            col += 1
            worksheet.update_cell(row, col, value)
            ticket_count = 1
if __name__ == "__main__":
    TICKET_DATA_URL = 'http:
    USERNAME = 'X'
    PASSWORD = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    CREDENTIALS_FILE = 'client_secret.json'
    SCOPE = ['https:
    TEMPLATE_FILE = 'qsdetemplate.csv'
    ticket_values = fetch_ticket_data(TICKET_DATA_URL, USERNAME, PASSWORD)
    gsheet_client = authorize_google_sheets(CREDENTIALS_FILE, SCOPE)
    update_google_sheet(gsheet_client, ticket_values, TEMPLATE_FILE)
    print("Google Sheets update complete.")
    sys.exit()