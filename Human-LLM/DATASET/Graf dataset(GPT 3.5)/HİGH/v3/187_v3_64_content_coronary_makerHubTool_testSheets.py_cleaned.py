from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.b12 import InstalledAppFlow
from google.auth.transport.b5 import Request
from printRequest import PrintRequest
b1 = []
b2 = []
b3 = []
b4 = []
b5 = [b2, b1, b3, b4]
b6 = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
b7 = ['https:
def fonk1():
    b8 = fonk2()
    b9 = build('sheets', 'v4', credentials=b8)
    b10 = b9.spreadsheets()
    b11 = fonk5(b10)
    if b11:
        fonk6(b11)
    else:
        print('No data found in the spreadsheet.')
def fonk2():
    b8 = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            b8 = pickle.load(token)
    if not b8 or not b8.valid:
        b8 = fonk3()
        fonk4(b8)
    return b8
def fonk3():
    b12 = InstalledAppFlow.from_client_secrets_file('credentials.json', b7)
    return b12.run_local_server()
def fonk4(b8):
    with open('token.pickle', 'wb') as token:
        pickle.dump(b8, token)
def fonk5(b10):
    b13 = b10.b11().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
                                b14 = 'Form Responses 1').execute()
    return b13.get('b11', [])
def fonk6(b11):
    for row_num, row in enumerate(b11, b15 = 1):
        b16 = PrintRequest(row, row_num)
        if b16.b17 = = '0':
            b2.append(b16)
        elif b16.b17 = = '1':
            b1.append(b16)
        elif b16.b17 = = '2':
            b3.append(b16)
        elif b16.b17 = = '3':
            b4.append(b16)
    fonk7()
def fonk7():
    while True:
        fonk8()
        b18 = fonk9()
        if b18 = = 'q':
            fonk11()
        elif b18 = = 'm':
            continue
        fonk10(b5[b18])
def fonk8():
    print('Options:')
    for idx, option in enumerate(b6):
        print(f'{option}[{idx}]')
def fonk9():
    print("Input selection: (q) to quit (m) to return to menu")
    b19 = input()
    if b19.lower() == 'q':
        return 'q'
    elif b19.lower() == 'm':
        return 'm'
    else:
        return int(b19)
def fonk10(lst):
    os.system('cls')
    print(f'\t NOW VIEWING {b6[b18]} \n')
    for idx, item in enumerate(lst):
        try:
            print(f'[{idx}] {str(item)}\n')
        except:
            print("Unable to print")
def fonk11():
    print('Exiting the program.')
    sys.exit()
if b20 = = '__main__':
    fonk1()