import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
ruser = 'X'
rpass = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
response = requests.get('http:
ticketdata = json.loads(response.text)
ticketvalue = []
for key, value in ticketdata.items():
    if isinstance(value, dict):
        for k, v in value.items():
            ticketvalue.append(v)
    else:
        ticketvalue.append(value)
scope = ['https:
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
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
sh.add_worksheet(title=str(daynow), rows="17", cols="25")
csv_template = open('qsdetemplate.csv', 'r').read()
shid = sh.id
client.import_csv(shid, csv_template)
worksheet = sh.get_worksheet(str(daynow))
r = 2
c = 2
tcount = 0
ttimer = 0
for x in ticketvalue:
    if tcount < 11:
        worksheet.update_cell(r, c, x)
        r += 1
        tcount += 1
        ttimer += 1
    elif tcount == 11:
        r = 2
        c += 1
        worksheet.update_cell(r, c, x)
        tcount = 0
        ttimer += 1
import sys
sys.exit()