import os
import re
import csv
import logging
import requests
import argparse
import datetime as dt
from bs4 import BeautifulSoup as bs
log = logging.getLogger(__name__)
logging.getLogger('pyactiveresource').setLevel(logging.WARNING)
def login_and_get(username, password):
    url = 'https:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    session = requests.Session()
    login_page = session.get(url, headers=headers)
    soup = bs(login_page.content, 'html.parser')
    data = {}
    input_fields = soup.find_all('input')
    for field in input_fields:
        name = field.get('name')
        value = field.get('value', '')
        typ = field.get('type')
        if typ == 'button':
            continue
        if name:
            data[name] = value
    data['Page$ctl08$Main$ctl04$form$loginUserName'] = username
    data['Page$ctl08$Main$ctl04$form$loginPassword'] = password[:20]
    response = session.post(url, data=data, headers=headers)
    return response
def get_data(content):
    soup = bs(content, 'html.parser')
    list_rentals = ['Date']
    list_wait_list_number = [dt.datetime.now().date().isoformat()]
    for row in soup.find_all(class_='row header'):
        rental_info = row.find_all('td')
        if len(rental_info) >= 8:
            list_rentals.append(rental_info[7].get_text().strip())
            list_wait_list_number.append(rental_info[19].get_text().strip())
    log.info('Found headers: %s', list_rentals)
    return list_rentals, list_wait_list_number
def save_data(data_to_save):
    file_path = 'data.csv'
    write_header = not os.path.exists(file_path) or os.stat(file_path).st_size == 0
    with open(file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if write_header:
            writer.writerow(data_to_save[0])
            log.info('Formatted data.csv with %d headers', len(data_to_save[0]))
        writer.writerow(data_to_save[1])
    log.info('Wrote data: %s', data_to_save[1])
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='KKIK Username', required=True)
    parser.add_argument('-p', '--password', help='KKIK Password', required=True)
    parser.add_argument('-l', '--log', help='Debug level', default='WARNING')
    args = parser.parse_args()
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {args.log}')
    logging.basicConfig(format='%(levelname)s\t%(message)s', level=numeric_level)
    response = login_and_get(args.username, args.password)
    if 'BoligÃ¸nsker' in response.text:
        log.info('Successfully logged in')
        data_to_save = get_data(response.content)
        save_data(data_to_save)
    else:
        log.error("Couldn't log in")
if __name__ == '__main__':
    main()