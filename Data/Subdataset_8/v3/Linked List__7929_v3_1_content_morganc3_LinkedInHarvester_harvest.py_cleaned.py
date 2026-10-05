import json
import re
import ssl
import argparse
from urllib.request import build_opener
from unidecode import unidecode
ssl._create_default_https_context = ssl._create_unverified_context
parser = argparse.ArgumentParser(description='Creates email addresses with optional formatters from names of employees of a company on LinkedIn.')
parser.add_argument('COMPANY', help='Company ID')
parser.add_argument('DOMAIN', help='Domain to be used in email address')
parser.add_argument('COOKIE', help='Cookie file', metavar="FILE")
parser.add_argument("-o", "--output", default='emails.txt', help="Path to output text file for emails")
parser.add_argument("-f", action="store_true", dest="abbrevF", default=False, help="Abbreviate first name")
parser.add_argument("-l", action="store_true", dest="abbrevL", default=False, help="Abbreviate last name")
parser.add_argument("-s", action="store_true", dest="swap", default=False, help="Switch order of first and last names")
args = parser.parse_args()
company_id = args.COMPANY
domain = args.DOMAIN
csrf_token = ''
session_id = ''
with open(args.COOKIE, "r") as f:
    csrf_token, session_id = [line.strip() for line in f]
cookie1 = 'li_at=' + session_id
cookie2 = 'JSESSIONID=' + csrf_token
creds = [
    'AAMS', 'ACA', 'ADPA', 'AIF', 'AWMA', 'CAIA', 'CAP', 'CDFA', 'CEP', 'CFA', 'CFP',
    'ChFC', 'CIMA', 'CLU', 'CPA', 'CMA', 'CMM', 'CMP', 'CDFA', 'CPWA', 'CRPC', 'CRPS',
    'CTP', 'CWS', 'Jr.', 'MBA', 'M.A.', 'RICP', 'Sr.', 'WMS'
]
def format_name(name):
    name = unidecode(name)
    pattern = r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*'
    match = re.match(pattern % ('|'.join([x[::-1] for x in creds])), name[::-1])
    if not match:
        print('Unexpected format for %s' % name)
    name = match.group(1)[::-1]
    final = re.subn(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not args.abbrevF and not args.abbrevL) else ''), '', name)[0].lower().split(' ')
    email = '.'.join(filter(lambda x: len(x) > 0, final)) + '@' + domain
    return email
def harvest(curr):
    url = ("https:
           "count=49&origin=OTHER&queryContext=List(spellCorrectionEnabled-%3Etrue,"
           "crelatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&q=all&filters=List(currentCompany-%3E" + company_id + ",resultType-%3EPEOPLE)&start=" + str(curr))
    opener = build_opener()
    opener.addheaders.extend([('csrf-token', csrf_token), ('Cookie', f'{cookie1};{cookie2}'), ('x-restli-protocol-version', '2.0.0')])
    response = opener.open(url)
    data = json.load(response)
    data = data["elements"][0]["elements"]
    return [format_name(f"{employee['image']['attributes'][0]['miniProfile']['firstName']} {employee['image']['attributes'][0]['miniProfile']['lastName']}") for employee in data if employee['image']['attributes'][0]['miniProfile']['firstName']]
emails = []
curr = 0
last_page = False
while not last_page:
    emails.extend(harvest(curr))
    curr += 49
    last_page = len(emails) % 49 != 0
with open(args.output, "w+") as f:
    for email in emails:
        try:
            f.write(f'{email}\n')
        except Exception as e:
            print(f'Error writing one email ("{email}") due to strange character: {e}')
print(f"Done! {len(emails)} emails have been written to {args.output}")