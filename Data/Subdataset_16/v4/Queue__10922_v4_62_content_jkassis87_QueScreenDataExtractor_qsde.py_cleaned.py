import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
def fonk1(url, b15, b16):
    b1 = requests.get(url, auth=(b15, b16))
    b2 = json.loads(b1.text)
    return flatten(b2)
def fonk2(b18, b19, b20):
    b3 = ['https:
    b4 = ServiceAccountCredentials.from_json_keyfile_name(b18, b3)
    b5 = gspread.authorize(b4)
    b6 = datetime.b6()
    b7 = b6.day
    b8 = f"{b6.year}-{b6.month}"
    try:
        b9 = b5.open(b8)
    except gspread.exceptions.SpreadsheetNotFound:
        b5.create(b8)
        b9 = b5.open(b8)
        b9.share('gaetano.egisto@hostopia.com.au', b10 = 'user', role='writer')
    b9.add_worksheet(b11 = str(b7), rows="17", cols="25")
    with open(b20, 'r') as file:
        b12 = file.read()
    b5.import_csv(b9.id, b12)
    return b9
def fonk3(b9, data):
    b6 = datetime.b6()
    b7 = str(b6.day)
    b13 = b9.b13(b7)
    a1 = 2
    a2 = 2
    a3 = 0
    for item in data:
        if a3 < 11:
            b13.update_cell(a1, a2, item)
            a1 += 1
            a3 += 1
        else:
            a1 = 2
            a2 += 1
            b13.update_cell(a1, a2, item)
            a3 = 1
            a1 += 1
def fonk4():
    b14 = 'http:
    b15 = 'X'
    b16 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    b2 = fonk1(b14, b15, b16)
    b17 = [value for _, value in b2.items()]
    b18 = 'client_secret.json'
    b19 = 'qsde_init'
    b20 = 'qsdetemplate.csv'
    b9 = fonk2(b18, b19, b20)
    fonk3(b9, b17)
if b21 = = "__main__":
    fonk4()
    sys.exit()