from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from printRequest import PrintRequest
SCOPES = ['https:
REQUESTS = {
    'TODO': [],
    'IN PROGRESS': [],
    'FINISHED': [],
    'FAILED': []
}
STATUS_OPTIONS = list(REQUESTS.keys())
def main():
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    spreadsheet_id = '1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24'
    range_name = 'Form Responses 1'
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        process_data(values)
        selector()
def get_credentials():
    creds = None
    token_path = 'token.pickle'
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return creds
def process_data(values):
    for row_num, row in enumerate(values, start=1):
        new_request = PrintRequest(row, row_num)
        status_key = STATUS_OPTIONS[int(new_request.status)]
        REQUESTS[status_key].append(new_request)
def selector():
    while True:
        print('\n'.join(f'{status}[{index}]' for index, status in enumerate(STATUS_OPTIONS)))
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
    status = STATUS_OPTIONS[choice]
    lst = REQUESTS[status]
    print(f'\t NOW VIEWING {status}\n')
    for index, item in enumerate(lst):
        try:
            print(f'[{index}] {item}\n')
        except Exception as e:
            print(f"Unable to print item {index}: {e}")
    list_menu(lst)
def list_menu(lst):
    choice = get_user_choice()
    if isinstance(choice, int):
        print(lst[choice])
if __name__ == '__main__':
    main()