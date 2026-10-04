from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from printRequest import PrintRequest
SCOPES = ['https:
TODO = []
IN_PROGRESS = []
FINISHED = []
FAILED = []
REQUESTS = [TODO, IN_PROGRESS, FINISHED, FAILED]
STATUS_OPTIONS = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
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
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24', range='Form Responses 1').execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        process_data(values)
def list_menu(lst):
    choice = get_user_choice()
    if isinstance(choice, int):
        print(lst[choice])
def selector():
    while True:
        print('TODO[0]\nIN PROGRESS[1]\nFINISHED[2]\nFAILED[3]')
        choice = get_user_choice()
        if isinstance(choice, str):
            continue
        display_list(choice)
def get_user_choice():
    print("Input selection: (q) to quit (m) to return to menu")
    user_input = input().strip().lower()
    if user_input == 'q':
        quit()
    elif user_input == 'm':
        return 'm'
    else:
        try:
            return int(user_input)
        except ValueError:
            return 'm'
def display_list(choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    lst = REQUESTS[choice]
    print(f'\t NOW VIEWING {STATUS_OPTIONS[choice]}\n')
    for index, item in enumerate(lst):
        try:
            print(f'[{index}] {item}\n')
        except Exception as e:
            print(f"Unable to print item {index}: {e}")
    list_menu(lst)
def process_data(values):
    for row_num, row in enumerate(values, start=1):
        new_request = PrintRequest(row, row_num)
        if new_request.status == '0':
            TODO.append(new_request)
        elif new_request.status == '1':
            IN_PROGRESS.append(new_request)
        elif new_request.status == '2':
            FINISHED.append(new_request)
        elif new_request.status == '3':
            FAILED.append(new_request)
    selector()
if __name__ == '__main__':
    main()