import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
def get_ticket_data_from_api(username, password):
    try:
        response = requests.get('http:
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Failed to fetch ticket data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching ticket data: {e}")
        return None
def authenticate_google_sheets(credentials_file):
    try:
        scope = ['https:
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        return gspread.authorize(creds)
    except Exception as e:
        print(f"Error authenticating with Google Sheets: {e}")
        return None
def main():
    ruser = 'X'
    rpass = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    ticket_data = get_ticket_data_from_api(ruser, rpass)
    if not ticket_data:
        sys.exit("Exiting script due to failure in fetching ticket data.")
    flattened_ticket_data = flatten(ticket_data)
    ticket_values = list(flattened_ticket_data.values())
    client = authenticate_google_sheets('client_secret.json')
    if not client:
        sys.exit("Exiting script due to failure in authenticating with Google Sheets.")
    now = datetime.now()
    day_now = now.day
    year_month = f"{now.year}-{now.month}"
    sh = client.open('qsde_init')
    if now.day == 1:
        sh = client.create(year_month)
        sh.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
    else:
        sh = client.open(year_month)
    worksheet = sh.add_worksheet(title=str(day_now), rows="17", cols="25")
    csv_template = open('qsdetemplate.csv', 'r').read()
    sh_id = sh.id
    client.import_csv(sh_id, csv_template)
    row = 2
    col = 2
    ticket_count = 0
    for value in ticket_values:
        if ticket_count < 11:
            worksheet.update_cell(row, col, value)
            row += 1
            ticket_count += 1
        elif ticket_count == 11:
            row = 2
            col += 1
            worksheet.update_cell(row, col, value)
            ticket_count = 0
    sys.exit()
if __name__ == "__main__":
    main()