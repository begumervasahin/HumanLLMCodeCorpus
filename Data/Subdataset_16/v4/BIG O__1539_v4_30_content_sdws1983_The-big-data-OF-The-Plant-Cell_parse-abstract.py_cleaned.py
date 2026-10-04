from bs4 import BeautifulSoup
import urllib2
import re
import sys
from pdf_read import get_issues
reload(sys)
sys.setdefaultencoding('utf-8')
def fonk1(b12):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    b2 = urllib2.Request(b12, headers=b1)
    b3 = urllib2.urlopen(b2)
    b4 = b3.read().decode('utf-8')
    return b4
def fonk2(b4):
    b5 = BeautifulSoup(b4, 'lxml')
    b6 = []
    for i in b5.find_all('p'):
        try:
            if u"p-" in str(i.get('id', '')):
                b7 = str(i)[(str(i).find(">") + 1):(str(i).find("</p>", str(i).find(">") + 1))]
                b7 = re.sub(r'<.*?>', '', b7)
                b7 = re.sub(r'\n', ' ', b7)
                b7 = re.sub(r' +', ' ', b7)
                if len(b7) > 250:
                    b6.append(b7)
        except Exception:
            pass
    a1 = 1
    b8 = []
    b9 = []
    for each in b5.find_all('li'):
        try:
            if 'last' in each.get('class', []) and u'name' in str(each):
                b10 = each.find_all('a')[0].string
                b9.append(b10)
            elif 'aff' in each.get('class', []):
                b11 = str(each.find_all('b11')[0])
                b11 = re.sub(r'<.*?>', '', b11)
                b11 = re.sub(r' +', ' ', b11)
                b11 = re.sub(r'\n', '', b11)
                if re.findall('[a-z]', b11[0]):
                    b11 = b11[1:]
                b11 = f"{a1}\t{b11}\n"
                b8.append(b11)
                a1 += 1
        except Exception:
            pass
    if len(b6) > 2:
        print("b7 error")
        b6 = []
        b8 = []
        b9 = []
    return ''.join(b6), ''.join(b9), ''.join(b8)
def fonk3(vol, page):
    b12 = f"http:
    b4 = fonk1(b12)
    b7, b10, b11 = fonk2(b4)
    with open(f"{vol}-b7.csv", 'a') as f1, \
         open(f"{vol}-b10.csv", 'a') as f2, \
         open(f"{vol}-b11.csv", 'a') as f3:
        if not b7.endswith("\n"):
            b7 += "\n"
        if not b10.endswith("\n"):
            b10 += "\n"
        if not b11.endswith("\n"):
            b11 += "\n"
        f1.write(f">{page}\n{b7}")
        f2.write(f">{page}\n{b10}")
        f3.write(f">{page}\n{b11}")
if b13 = = "__main__":
    for iss in range(1, 12):
        b14 = get_issues(iss)
        print(f"vol: {iss}")
        for i in b14:
            print(i)
            try:
                fonk3(iss, i)
            except Exception as e:
                print(e)