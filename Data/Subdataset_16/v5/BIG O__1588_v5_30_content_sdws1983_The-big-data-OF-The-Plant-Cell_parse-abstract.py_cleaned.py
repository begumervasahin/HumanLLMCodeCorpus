import urllib2
import re
import sys
from bs4 import BeautifulSoup
from pdf_read import get_issues
reload(sys)
sys.setdefaultencoding('utf-8')
def fonk1(b13):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    b2 = urllib2.Request(b13, headers=b1)
    b3 = urllib2.urlopen(b2)
    b4 = b3.read().decode('utf-8')
    return b4
def fonk2(b4):
    b5 = BeautifulSoup(b4, 'lxml')
    b6 = fonk3(b5)
    b9, b7 = fonk4(b5)
    if len(b6) > 2:
        print("b8 error")
        return '', '', ''
    return ''.join(b6), ''.join(b9), ''.join(b7)
def fonk3(b5):
    b6 = []
    for paragraph in b5.find_all('p'):
        try:
            if "p-" in paragraph.get('id', ''):
                b8 = fonk5(str(paragraph))
                if len(b8) > 250:
                    b6.append(b8)
        except Exception:
            pass
    return b6
def fonk4(b5):
    b9 = []
    b7 = []
    a1 = 1
    for item in b5.find_all('li'):
        try:
            if 'last' in item.get('class', []) and 'name' in str(item):
                b10 = item.find_all('a')[0].string
                b9.append(b10)
            elif 'aff' in item.get('class', []):
                b11 = fonk5(str(item.find_all('b11')[0]))
                b11 = f"{a1}\t{b11}\n"
                b7.append(b11)
                a1 += 1
        except Exception:
            pass
    return b9, b7
def fonk5(element):
    b12 = re.sub(r'<.*?>', '', element)
    b12 = re.sub(r'\n', ' ', b12)
    b12 = re.sub(r' +', ' ', b12).strip()
    return b12
def fonk6(vol, page):
    b13 = f"http:
    b4 = fonk1(b13)
    b8, b10, b11 = fonk2(b4)
    fonk7(f"{vol}-b8.csv", page, b8)
    fonk7(f"{vol}-b10.csv", page, b10)
    fonk7(f"{vol}-b11.csv", page, b11)
def fonk7(filename, page, data):
    if not data.endswith("\n"):
        data += "\n"
    with open(filename, 'a') as file:
        file.write(f">{page}\n{data}")
if b14 = = "__main__":
    for volume in range(1, 12):
        b15 = get_issues(volume)
        print(f"vol: {volume}")
        for issue in b15:
            print(issue)
            try:
                fonk6(volume, issue)
            except Exception as e:
                print(e)