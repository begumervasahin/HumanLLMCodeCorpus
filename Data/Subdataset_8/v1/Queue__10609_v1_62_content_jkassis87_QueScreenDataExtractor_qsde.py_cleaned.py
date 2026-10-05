import requests
import json
from flatten_dict import flatten
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
def main():
    ruser = 'X'
    rpass = '5rsMThTeZ22p3MqGpz2xRPGY5hAWrwmx'
    get_ticket_data = requests.get('http:
    ticket_data = json.loads(get_ticket_data.text)
    ticket_data = flatten(ticket_data)
    ticket_values = list(ticket_data.values())
    scope = ['https:
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    now = datetime.now()
    day_now = now.day
    year_month = f"{now.year}-{now.month}"
    sh = client.open('qsde_init')
    if now.day == 1:
        sh.client.create(year_month)
        sh = client.open(year_month)
        sh.share('gaetano.egisto@hostopia.com.au', perm_type='user', role='writer')
    sh = client.open(year_month)
    sh.add_worksheet(title=str(day_now), rows="17", cols="25")
    csv_template = open('qsdetemplate.csv', 'r').read()
    sh_id = sh.id
    client.import_csv(sh_id, csv_template)
    worksheet = sh.get_worksheet(str(day_now))
    r = 2
    c = 2
    t_count = 0
    for x in ticket_values:
        if t_count < 11:
            worksheet.update_cell(r, c, x)
            r += 1
            t_count += 1
        elif t_count == 11:
            r = 2
            c += 1
            worksheet.update_cell(r, c, x)
            t_count = 0
    sys.exit()
if __name__ == "__main__":
    main()