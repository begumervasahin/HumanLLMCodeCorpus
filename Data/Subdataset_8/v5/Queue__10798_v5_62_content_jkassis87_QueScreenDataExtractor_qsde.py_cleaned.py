import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
API_URL = 'http:
API_USER = 'X'
API_PASSWORD = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
response = requests.get(API_URL, auth=(API_USER, API_PASSWORD))
ticketdata = json.loads(response.text)
ticketvalue = []
for key, value in ticketdata.items():
    if isinstance(value, dict):
        ticketvalue.extend(value.values())
    else:
        ticketvalue.append(value)
SCOPE = ['https:
CREDS_FILE = 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
client = gspread.authorize(creds)
now = datetime.now()
daynow = now.day
yearmonth = f"{now.year}-{now.month}"
sh = client.open('qsde_init')
if now.day == 1:
    sh = client.create(yearmonth)
    sh.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
else:
    sh = client.open(yearmonth)
worksheet = sh.add_worksheet(title=str(daynow), rows="17", cols="25")
csv_template = open('qsdetemplate.csv', 'r').read()
sh_id = sh.id
client.import_csv(sh_id, csv_template)
row, col = 2, 2
ticket_count = 0
for value in ticketvalue:
    if ticket_count < 11:
        worksheet.update_cell(row, col, value)
        row += 1
        ticket_count += 1
    else:
        row, col = 2, col + 1
        worksheet.update_cell(row, col, value)
        ticket_count = 0
import sys
sys.exit()