from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.b15 import InstalledAppFlow
from google.auth.transport.b5 import Request
from printRequest import PrintRequest
b1 = []
b2 = []
b3 = []
b4 = []
b5 = [b1, b2, b3, b4]
b6 = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
b7 = ['https:
def fonk1():
    b8 = fonk2()
    b9 = build('sheets', 'v4', credentials=b8)
    b10 = b9.spreadsheets()
    b11 = b10.b14().get(
        b12 = '1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
        b13 = 'Form Responses 1'
    ).execute()
    b14 = b11.get('b14', [])
    if not b14:
        print('No data found.')
    else:
        fonk7(b14)
def fonk2():
    b8 = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            b8 = pickle.load(token)
    if not b8 or not b8.valid:
        if b8 and b8.expired and b8.refresh_token:
            b8.refresh(Request())
        else:
            b15 = InstalledAppFlow.from_client_secrets_file('credentials.json', b7)
            b8 = b15.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(b8, token)
    return b8
def fonk3(b19):
    b16 = fonk5()
    if isinstance(b16, int):
        print(b19[b16])
def fonk4():
    while True:
        print('TODO[0]\nIN PROGRESS[1]\nFINISHED[2]\nFAILED[3]')
        b16 = fonk5()
        if isinstance(b16, str):
            continue
        fonk6(b16)
def fonk5():
    b17 = input("Input selection: (q) to quit (m) to return to menu: ").lower()
    if b17 = = 'q':
        quit()
    elif b17 = = 'm':
        return 'm'
    else:
        try:
            return int(b17)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return fonk5()
def fonk6(b16):
    os.system('cls' if os.b18 = = 'nt' else 'clear')
    b19 = b5[b16]
    print(f'\t NOW VIEWING {b6[b16]}\n')
    for idx, item in enumerate(b19):
        try:
            print(f'[{idx}] {item}\n')
        except Exception as e:
            print(f"Unable to print: {e}")
    fonk3(b19)
def fonk7(b14):
    a1 = 1
    for row in b14:
        b20 = PrintRequest(row, a1)
        a1 += 1
        if b20.b21 = = '0':
            b1.append(b20)
        elif b20.b21 = = '1':
            b2.append(b20)
        elif b20.b21 = = '2':
            b3.append(b20)
        elif b20.b21 = = '3':
            b4.append(b20)
    fonk4()
if b22 = = '__main__':
    fonk1()