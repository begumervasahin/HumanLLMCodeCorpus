from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from printRequest import PrintRequest
inProgress = []
todo = []
finished = []
failed = []
requests = [todo, inProgress, finished, failed]
options = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
SCOPES = ['https:
def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
                                range='Form Responses 1').execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        make_sets(values)
def list_menu(lst):
    choice = num_input()
    if type(choice) != str:
        print(lst[choice])
def selector():
    while True:
        print('TODO[0]\nPROGRESS[1]\nFINISHED[2]\nFAILED[3]')
        choice = num_input()
        if type(choice) == str:
            continue
        print_list(choice)
def num_input():
    print("Input selection: (q) to quit (m) to return to menu")
    to_return = input()
    if to_return.lower() == 'q':
        quit()
    elif to_return.lower() == 'm':
        return 'm'
    else:
        return int(to_return)
def print_list(choice):
    os.system('cls')
    lst = requests[choice]
    print('\t NOW VIEWING ' + options[choice] + '\n')
    for idx, item in enumerate(lst):
        try:
            print(f'[{idx}] {str(item)}\n')
        except:
            print("Unable to print")
    list_menu(lst)
def make_sets(values):
    row_num = 1
    for row in values:
        new_request = PrintRequest(row, row_num)
        row_num += 1
        if new_request.status == '0':
            todo.append(new_request)
        elif new_request.status == '1':
            inProgress.append(new_request)
        elif new_request.status == '2':
            finished.append(new_request)
        elif new_request.status == '3':
            failed.append(new_request)
    selector()
if __name__ == '__main__':
    main()