import os
import re
import csv
import logging
import requests
import argparse
import datetime as dt
from bs4 import BeautifulSoup as bs
logging.basicConfig(format='%(levelname)s\t%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
logging.getLogger('pyactiveresource').setLevel(logging.WARNING)
def login_and_fetch_data(username, password):
    login_url = 'https:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    session = requests.Session()
    response = session.get(login_url)
    soup = bs(response.content, 'html.parser')
    form_data = {}
    input_fields = re.findall('<input(.*)>', response.text, flags=re.IGNORECASE)
    for field in input_fields:
        name = re.findall('.*name="([^"]*)".*', field)
        value = re.findall('.*value="([^"]*)".*', field)
        typ = re.findall('.*type="([^"]*)".*', field)
        if typ[0] == 'button':
            continue
        if name:
            form_data[name[0]] = value[0] if value else ""
    form_data['Page$ctl08$Main$ctl04$form$loginUserName'] = username
    form_data['Page$ctl08$Main$ctl04$form$loginPassword'] = password[:20]
    login_response = session.post(login_url, data=form_data, headers=headers, params={'Referer': response.url})
    return session, login_response
def fetch_data(session, url):
    rental_data = []
    wait_list_numbers = []
    response = session.get(url)
    soup = bs(response.content, 'html.parser')
    rental_data.append('Date')
    rental_data.append(dt.datetime.now().date().isoformat())
    for item in soup.find_all(class_='row header'):
        rental_data.append(item.contents[7].get_text().strip())
        wait_list_numbers.append(item.contents[19].get_text().strip())
    log.info(f'Found\n{rental_data}')
    return rental_data, wait_list_numbers
def save_data(data_to_save):
    file_path = 'data.csv'
    with open(file_path, 'a') as csv_file:
        if os.stat(file_path).st_size <= 0:
            header_writer = csv.DictWriter(csv_file, fieldnames=data_to_save[0])
            header_writer.writeheader()
            log.info('Formatted data.csv with %d headers', len(data_to_save[0]))
        row_writer = csv.writer(csv_file)
        row_writer.writerow(data_to_save[1])
    log.info('Wrote data:\n%s', data_to_save[1])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='KKIK Username', required=True)
    parser.add_argument('-p', '--password', help='KKIK Password', required=True)
    parser.add_argument('-l', '--log', help='Debug level', default='WARNING')
    args = parser.parse_args()
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log)
    session, login_response = login_and_fetch_data(args.username, args.password)
    if 'BoligÃ¸nsker' in login_response.text:
        log.info('Successfully logged in')
        data_to_save = fetch_data(session, login_response.content)
        save_data(data_to_save)
    else:
        log.error('Couldn\'t log in')