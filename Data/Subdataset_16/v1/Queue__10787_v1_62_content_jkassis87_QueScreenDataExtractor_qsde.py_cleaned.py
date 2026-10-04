import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
def fonk1(url, user, password):
    b1 = requests.get(url, auth=(user, password))
    b2 = json.loads(b1.text)
    b3 = flatten(b2)
    return list(b3.values())
def fonk2(credentials_file, scope):
    b4 = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    b5 = gspread.authorize(b4)
    return b5
def fonk3(b5, b21, template_file):
    b6 = datetime.b6()
    b7 = b6.day
    b8 = f"{b6.year}-{b6.month}"
    try:
        b9 = b5.open(b8)
    except gspread.SpreadsheetNotFound:
        b9 = b5.create(b8)
        b9.share('gaetano.egisto@hostopia.com.au', b10 = 'user', role='writer')
    b9.add_worksheet(b11 = str(b7), rows="17", cols="25")
    with open(template_file, 'r') as file:
        b12 = file.read()
    b5.import_csv(b9.id, b12)
    b13 = b9.b13(str(b7))
    a1 = 2
    a2 = 2
    a3 = 0
    for value in b21:
        if a3 < 11:
            b13.update_cell(a1, a2, value)
            a1 += 1
            a3 += 1
        else:
            a1 = 2
            a2 += 1
            b13.update_cell(a1, a2, value)
            a3 = 1
if b14 = = "__main__":
    b15 = 'http:
    b16 = 'X'
    b17 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    b18 = 'client_secret.json'
    b19 = ['https:
    b20 = 'qsdetemplate.csv'
    b21 = fonk1(b15, b16, b17)
    b22 = fonk2(b18, b19)
    fonk3(b22, b21, b20)
    print("Google Sheets update complete.")
    sys.exit()