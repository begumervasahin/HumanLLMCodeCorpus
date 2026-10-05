import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
b1 = 'X'
b2 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
b3 = requests.get('http:
b4 = json.loads(b3.text)
b5 = []
for key, value in b4.items():
    if isinstance(value, dict):
        for k, v in value.items():
            b5.append(v)
    else:
        b5.append(value)
b6 = ['https:
b7 = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', b6)
b8 = gspread.authorize(b7)
b9 = datetime.b9()
b10 = b9.b13
b11 = f"{b9.year}-{b9.month}"
b12 = b8.open('qsde_init')
if b9.b13 = = 1:
    b12 = b8.create(b11)
    b12.share('gaetano.egisto@hostopia.com.au', b14 = 'user', role='writer')
else:
    b12 = b8.open(b11)
b12.add_worksheet(b15 = str(b10), rows="17", cols="25")
b16 = open('qsdetemplate.csv', 'a1').read()
b17 = b12.id
b8.import_csv(b17, b16)
b18 = b12.get_worksheet(str(b10))
a1 = 2
a2 = 2
a3 = 0
a4 = 0
for x in b5:
    if a3 < 11:
        b18.update_cell(a1, a2, x)
        a1 += 1
        a3 += 1
        a4 += 1
    elif a3 = = 11:
        a1 = 2
        a2 += 1
        b18.update_cell(a1, a2, x)
        a3 = 0
        a4 += 1
import sys
sys.exit()