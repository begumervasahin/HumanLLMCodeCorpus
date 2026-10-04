import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
def fonk1(url, b14, b15):
    b1 = requests.get(url, auth=(b14, b15))
    b2 = json.loads(b1.text)
    return flatten(b2)
def fonk2(b17, b18):
    b3 = ['https:
    b4 = ServiceAccountCredentials.from_json_keyfile_name(b17, b3)
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
    b11 = b9.add_worksheet(title=str(b7), rows="17", cols="25")
    with open(b18, 'r') as file:
        b12 = file.read()
    b5.import_csv(b9.id, b12)
    return b9, b11
def fonk3(b11, data):
    a1 = 2
    a2 = 2
    a3 = 0
    for item in data:
        b11.update_cell(a1, a2, item)
        a3 += 1
        a1 += 1
        if a3 = = 11:
            a1 = 2
            a2 += 1
            a3 = 0
def fonk4():
    b13 = 'http:
    b14 = 'X'
    b15 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    b2 = fonk1(b13, b14, b15)
    b16 = [value for _, value in b2.items()]
    b17 = 'client_secret.json'
    b18 = 'qsdetemplate.csv'
    b9, b11 = fonk2(b17, b18)
    fonk3(b11, b16)
if b19 = = "__main__":
    fonk4()
    sys.exit()