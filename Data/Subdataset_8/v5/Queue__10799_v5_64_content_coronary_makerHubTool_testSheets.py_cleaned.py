from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from printRequest import PrintRequest
STATUS_TODO = '0'
STATUS_IN_PROGRESS = '1'
STATUS_FINISHED = '2'
STATUS_FAILED = '3'
STATUS_OPTIONS = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
todo = []
in_progress = []
finished = []
failed = []
requests = [todo, in_progress, finished, failed]
SCOPES = ['https:
def main():
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    values = get_spreadsheet_values(service)
    if not values:
        print('No data found.')
    else:
        make_sets(values)
def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        creds = refresh_credentials(creds)
    return creds
def refresh_credentials(creds):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server()
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    return creds
def get_spreadsheet_values(service):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
                                range='Form Responses 1').execute()
    return result.get('values', [])
def make_sets(values):
    for row_num, row in enumerate(values, 1):
        new_request = PrintRequest(row, row_num)
        categorize_request(new_request)
def categorize_request(request):
    status = request.status
    if status == STATUS_TODO:
        todo.append(request)
    elif status == STATUS_IN_PROGRESS:
        in_progress.append(request)
    elif status == STATUS_FINISHED:
        finished.append(request)
    elif status == STATUS_FAILED:
        failed.append(request)
def selector():
    while True:
        print_options()
        choice = get_numeric_input()
        if isinstance(choice, int):
            print_list(choice)
def print_options():
    for idx, option in enumerate(STATUS_OPTIONS):
        print(f'{option}[{idx}]')
def get_numeric_input():
    print("Input selection: (q) to quit (m) to return to menu")
    user_input = input()
    if user_input.lower() == 'q':
        quit()
    elif user_input.lower() == 'm':
        return 'm'
    else:
        try:
            return int(user_input)
        except ValueError:
            pass
def print_list(choice):
    os.system('cls')
    request_list = requests[choice]
    print(f'\t NOW VIEWING {STATUS_OPTIONS[choice]}\n')
    for idx, request in enumerate(request_list):
        try:
            print(f'[{idx}] {str(request)}\n')
        except:
            print("Unable to print")
    list_menu(request_list)
def list_menu(request_list):
    choice = get_numeric_input()
    if isinstance(choice, int):
        print(request_list[choice])
if __name__ == '__main__':
    main()