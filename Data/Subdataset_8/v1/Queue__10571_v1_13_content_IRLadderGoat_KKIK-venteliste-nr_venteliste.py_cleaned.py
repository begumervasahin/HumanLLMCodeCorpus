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
def login_and_get(username, password):
    url = 'https:
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    session = requests.Session()
    site = session.get(url)
    soup = bs(site.content, 'html.parser')
    data = {}
    input_fields = re.findall('<input(.*)>', site.text, flags=re.IGNORECASE)
    for field in input_fields:
        name = re.findall('.*name="([^"]*)".*',field)
        value = re.findall('.*value="([^"]*)".*',field)
        typ = re.findall('.*type="([^"]*)".*',field)
        if typ[0] =='button':
            continue
        if name:
            if value:
                data[name[0]] = value[0]
            else:
                data[name[0]] = ""
    data['Page$ctl08$Main$ctl04$form$loginUserName'] = username
    data['Page$ctl08$Main$ctl04$form$loginPassword'] = password[:20]
    r = session.post(url, data=data, headers=request_headers, params={'Referer': site.url})
    return r
def get_data(url):
    list_rentals = []
    list_wait_list_number = []
    soup = bs(url, 'html.parser')
    list_rentals.append('Date')
    list_wait_list_number.append(dt.datetime.now().date().isoformat())
    for i in soup.find_all(class_='row header'):
        list_rentals.append(i.contents[7].get_text().strip())
        list_wait_list_number.append(i.contents[19].get_text().strip())
    log.info(f'Found\n{list_rentals}')
    return (list_rentals, list_wait_list_number)
def save_data(data_to_save):
    with open('data.csv', 'a') as csv_file:
        if os.stat('data.csv').st_size <= 0:
            head_writer = csv.DictWriter(csv_file, fieldnames=data_to_save[0])
            head_writer.writeheader()
            log.info('formatted data.csv with %d headers', len(data_to_save[0]))
        row_writer = csv.writer(csv_file)
        row_writer.writerow(data_to_save[1])
    log.info('Wrote data:\n%s', data_to_save[1])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='KKIK Username', required=True)
    parser.add_argument('-p', '--password', help='KKIK Password', required=True)
    parser.add_argument('-l', '--log', help='Debug level', default='WARNING',)
    args = parser.parse_args()
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log)
    response = login_and_get(args.username, args.password)
    if 'BoligÃ¸nsker' in response.text:
        log.info('Succesfully logged in')
        save_data(get_data(response.content))
    else:
        log.error('Couldn\'t log in')