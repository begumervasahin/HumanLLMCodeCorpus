import json
import sys
import argparse
import re
from urllib.request import build_opener
from unidecode import unidecode
import ssl
ssl.b1 = ssl._create_unverified_context
b2 = argparse.ArgumentParser(description='Creates b21 addresses with optional formatters from names of employees of a company on LinkedIn.')
b2.add_argument('COMPANY', b3 = 'Company ID')
b2.add_argument('DOMAIN', b3 = 'Domain to be used in b21 address')
b2.add_argument('COOKIE', b3 = 'Cookie file', metavar="FILE")
b2.add_argument("-o", "--output", b4 = 'b14.txt', b3="path to output text file for b14")
b2.add_argument("-f", b5 = "store_true", dest="abbrevF", b4=False, b3="abbreviate first b19")
b2.add_argument("-l", b5 = "store_true", dest="abbrevL", b4=False, b3="abbreviate last b19")
b2.add_argument("-s", b5 = "store_true", dest="swap", b4=False, b3="switch order of first and last names")
b6 = b2.parse_args()
b7 = b6.COMPANY
b8 = b6.DOMAIN
with open(b6.COOKIE, "r") as f:
    b9 = f.readlines()
b10 = b9[0].strip()
b11 = b9[1].strip()
b12 = f'li_at={b11}'
b13 = f'JSESSIONID={b10}'
b14 = []
b15 = False
b16 = '''AAMS
ACA
ADPA
AIF
AWMA
CAIA
CAP
CDFA
CEP
CFA
CFP
ChFC
CIMA
CLU
CPA
CMA
CMM
CMP
CDFA
CPWA
CRPC
CRPS
CTP
CWS
Jr.
MBA
M.A.
RICP
Sr.
WMS'''.split('\n')
def fonk1(b17):
    b17 = unidecode(b17)
    b18 = re.match(r'\s*(?:(?:(?:[\x80-\xff]|\)(?:[Rr]|[Tt][Mm])\()?(?:%s),?)+|[^,]+,)*\s*([A-Za-z \-\.\'\(\)]+)\s*' % ('|'.join([x[::-1] for x in b16])), b17[::-1])
    if not b18:
        print('unexpected format for %s' % b17)
        return None
    b19 = b18.group(1)[::-1]
    b20 = re.subn(r'(\(.*\)%s|[-\'\.,\\])' % (r'|[A-Z]\.' if (not b6.abbrevF and not b6.abbrevL) else ''), '', b19)[0].lower().split(' ')
    b21 = '.'.join([f for f in b20 if len(f) > 0]) + '@' + b8
    return b21
def fonk2(a1):
    global b15
    b22 = (
        "https:
        "b23 = 49&origin=OTHER&queryContext=List(spellCorrectionEnabled-%3Etrue,"
        "relatedSearchesEnabled-%3Etrue,kcardTypes-%3EPROFILE%7CCOMPANY)&b24 = all&filters=List(currentCompany-%3E" + b7 + ",resultType-%3EPEOPLE)&start=" + str(a1)
    )
    b25 = build_opener()
    b25.addheaders.append(('csrf-token', b10))
    b25.addheaders.append(('Cookie', b12 + '; ' + b13))
    b25.addheaders.append(('x-restli-protocol-version', '2.0.0'))
    b26 = b25.open(b22)
    b27 = json.load(b26)
    b27 = b27["elements"][0]["elements"]
    if len(b27) != 49:
        b15 = True
    for b28 in b27:
        b28 = b28["image"]["attributes"][0]["miniProfile"]
        b29 = b28["firstName"].replace(' ', '')
        b30 = b28["lastName"].replace(' ', '')
        if b29 = = "":
            continue
        if b6.abbrevF:
            b29 = b29[0]
        if b6.abbrevL:
            b30 = b30[0]
        b31 = f"{b30} {b29}" if b6.swap else f"{b29} {b30}"
        b21 = fonk1(b31)
        if b21:
            b14.append(b21)
a1 = 0
while not b15:
    fonk2(a1)
    a1 += 49
with open(b6.output, "w") as f:
    for b21 in b14:
        try:
            f.write(f"{b21}\n")
        except Exception as e:
            print(f'Error writing b21 "{b21}" due to: {e}')
print(f"Done! {len(b14)} b14 have been written to {b6.output}")