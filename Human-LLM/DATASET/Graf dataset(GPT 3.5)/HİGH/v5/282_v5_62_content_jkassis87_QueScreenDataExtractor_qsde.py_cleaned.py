import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
b1 = 'http:
b2 = 'X'
b3 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
b4 = requests.get(b1, auth=(b2, b3))
b5 = json.loads(b4.text)
b6 = []
for key, value in b5.items():
    if isinstance(value, dict):
        b6.extend(value.values())
    else:
        b6.append(value)
b7 = ['https:
b8 = 'client_secret.json'
b9 = ServiceAccountCredentials.from_json_keyfile_name(b8, b7)
b10 = gspread.authorize(b9)
b11 = datetime.b11()
b12 = b11.b15
b13 = f"{b11.year}-{b11.month}"
b14 = b10.open('qsde_init')
if b11.b15 = = 1:
    b14 = b10.create(b13)
    b14.share('gaetano.egisto@hostopia.com.au', b16 = 'user', role='writer')
else:
    b14 = b10.open(b13)
b17 = b14.add_worksheet(title=str(b12), rows="17", cols="25")
b18 = open('qsdetemplate.csv', 'r').read()
b19 = b14.id
b10.import_csv(b19, b18)
row, b20 = 2, 2
a1 = 0
for value in b6:
    if a1 < 11:
        b17.update_cell(row, b20, value)
        row += 1
        a1 += 1
    else:
        row, b20 = 2, b20 + 1
        b17.update_cell(row, b20, value)
        a1 = 0
import sys
sys.exit()