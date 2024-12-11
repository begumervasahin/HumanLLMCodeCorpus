import json
import sys
import argparse
import re
import ssl
from urllib.request import build_opener
from unidecode import unidecode
ssl.b1 = ssl._create_unverified_context
b2 = argparse.ArgumentParser(description='Creates b22 addresses with optional formatters from names of employees of a company on LinkedIn.')
b2.add_argument('COMPANY', b3 = 'Company ID')
b2.add_argument('DOMAIN', b3 = 'Domain to be used in b22 address')
b2.add_argument('COOKIE', b3 = 'Cookie file', metavar="FILE")
b2.add_argument("-o", "--output", b4 = 'b14.txt', b3="Path to output text file for b14")
b2.add_argument("-f", b5 = "store_true", dest="abbrevF", b4=False, b3="Abbreviate first b20")
b2.add_argument("-l", b5 = "store_true", dest="abbrevL", b4=False, b3="Abbreviate last b20")
b2.add_argument("-s", b5 = "store_true", dest="swap", b4=False, b3="Switch order of first and last names")
b6 = b2.parse_args()
b7 = b6.COMPANY
b8 = b6.DOMAIN
b9 = ''
b10 = ''
with open(b6.COOKIE, "r") as f:
    b11 = f.readlines()
    b9 = b11[0][:-1]
    b10 = b11[1][:-1]
b12 = 'li_at=' + b10
b13 = 'JSESSIONID=' + b9
b14 = []
b15 = False
b16 = [
    'AAMS', 'ACA', 'ADPA', 'AIF', 'AWMA', 'CAIA', 'CAP', 'CDFA', 'CEP', 'CFA', 'CFP',
    'ChFC', 'CIMA', 'CLU', 'CPA', 'CMA', 'CMM', 'CMP', 'CDFA', 'CPWA', 'CRPC', 'CRPS',
    'CTP', 'CWS', 'Jr.', 'MBA', 'M.A.', 'RICP', 'Sr.', 'WMS'
]
def fonk1(b17):
    b17 = unidecode(b17)
    b18 = r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*'
    b19 = re.match(b18 % ('|'.join([x[::-1] for x in b16])), b17[::-1])
    if not b19:
        print('Unexpected format for %s' % b17)
    b20 = b19.group(1)[::-1]
    b21 = re.subn(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not b6.abbrevF and not b6.abbrevL) else ''), '', b20)[0].lower().split(' ')
    b22 = '.'.join([f for f in b21 if len(f) > 0]) + '@' + b8
    return b22
def fonk2(a1):
    global b15
    b23 = ("https:
           "b24 = 49&origin=OTHER&queryContext=List(spellCorrectionEnabled-%3Etrue,"
           "crelatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&b25 = all&filters=List(currentCompany-%3E" + b7 + ",resultType-%3EPEOPLE)&start=" + str(a1))
    b26 = build_opener()
    b26.addheaders.append(('csrf-token', b9))
    b26.addheaders.append(('Cookie', b12 + ';' + b13))
    b26.addheaders.append(('x-restli-protocol-version', '2.0.0'))
    b27 = b26.open(b23)
    b28 = json.load(b27)
    b28 = b28["elements"][0]
    b28 = b28["elements"]
    if len(b28) != 49:
        b15 = True
    for b29 in b28:
        b29 = b29["image"]["attributes"][0]["miniProfile"]
        b30 = b29["firstName"].replace(' ', '')
        b31 = b29["lastName"].replace(' ', '')
        if b30 = = "":
            continue
        if b6.abbrevF:
            b30 = b30[0:1]
        if b6.abbrevL:
            b31 = b31[0:1]
        if b6.swap:
            b32 = b31 + ' ' + b30
        else:
            b32 = b30 + ' ' + b31
        b22 = fonk1(b32)
        b14.append(b22)
a1 = 0
while not b15:
    fonk2(a1)
    a1 = a1 + 49
with open(b6.output, "w+") as f:
    b24 = len(b14)
    for i in b14:
        try:
            f.write('%s\n' % i)
        except:
            print('Error writing one b22 ("%s") due to strange character' % i)
print("Done! " + str(b24) + " b14 have been written to %s" % b6.output)