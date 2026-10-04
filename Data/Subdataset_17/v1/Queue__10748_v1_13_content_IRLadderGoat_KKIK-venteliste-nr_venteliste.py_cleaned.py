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
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    s = requests.Session()
    site = s.get(url)
    soup = bs(site.content, 'html.parser')
    data = {}
    input_fields = re.findall('<input(.*)>', site.text, flags=re.IGNORECASE)
    for field in input_fields:
        name = re.findall('.*name="([^"]*)".*', field)
        value = re.findall('.*value="([^"]*)".*', field)
        typ = re.findall('.*type="([^"]*)".*', field)
        if typ and typ[0] == 'button':
            continue
        if name:
            data[name[0]] = value[0] if value else ""
    data['Page$ctl08$Main$ctl04$form$loginUserName'] = username
    data['Page$ctl08$Main$ctl04$form$loginPassword'] = password[:20]
    response = s.post(url, data=data, headers=request_headers, params={'Referer': site.url})
    return response
def get_data(content):
    list_rentals = ['Date']
    list_wait_list_number = [dt.datetime.now().date().isoformat()]
    soup = bs(content, 'html.parser')
    for row in soup.find_all(class_='row header'):
        list_rentals.append(row.contents[7].get_text().strip())
        list_wait_list_number.append(row.contents[19].get_text().strip())
    log.info(f'Found\n{list_rentals}')
    return list_rentals, list_wait_list_number
def save_data(data_to_save):
    file_path = 'data.csv'
    write_header = not os.path.exists(file_path) or os.stat(file_path).st_size == 0
    with open(file_path, 'a', newline='') as csvFile:
        if write_header:
            head_writer = csv.DictWriter(csvFile, fieldnames=data_to_save[0])
            head_writer.writeheader()
            log.info('Formatted data.csv with %d headers', len(data_to_save[0]))
        row_writer = csv.writer(csvFile)
        row_writer.writerow(data_to_save[1])
    log.info('Wrote data:\n%s', data_to_save[1])
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
        log.error('Couldn\'t log in')
if __name__ == '__main__':
    main()