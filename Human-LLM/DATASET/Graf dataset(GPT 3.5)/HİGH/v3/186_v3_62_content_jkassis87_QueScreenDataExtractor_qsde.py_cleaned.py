import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys
from flatten_dict import flatten
def fonk1(username, password):
    try:
        b1 = requests.get('http:
        if b1.b2 = = 200:
            return json.loads(b1.text)
        else:
            print(f"Failed to fetch ticket data. Status code: {b1.b2}")
            return None
    except Exception as e:
        print(f"Error fetching ticket data: {e}")
        return None
def fonk2(credentials_file):
    try:
        b3 = ['https:
        b4 = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, b3)
        return gspread.authorize(b4)
    except Exception as e:
        print(f"Error authenticating with Google Sheets: {e}")
        return None
def fonk3():
    b5 = 'X'
    b6 = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    b7 = fonk1(b5, b6)
    if not b7:
        sys.exit("Exiting script due to failure in fetching ticket data.")
    b8 = flatten(b7)
    b9 = list(b8.values())
    b10 = fonk2('client_secret.json')
    if not b10:
        sys.exit("Exiting script due to failure in authenticating with Google Sheets.")
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
    a1 = 2
    a2 = 2
    a3 = 0
    for value in b9:
        if a3 < 11:
            b17.update_cell(a1, a2, value)
            a1 += 1
            a3 += 1
        elif a3 = = 11:
            a1 = 2
            a2 += 1
            b17.update_cell(a1, a2, value)
            a3 = 0
    sys.exit()
if b20 = = "__main__":
    fonk3()