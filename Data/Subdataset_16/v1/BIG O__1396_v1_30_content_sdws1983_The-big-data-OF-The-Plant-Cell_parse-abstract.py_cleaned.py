import requests
from bs4 import BeautifulSoup
import re
import sys
def fonk1(b11):
    b1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    b2 = requests.get(b11, b1=b1)
    b2.b3 = 'utf-8'
    return b2.text
def fonk2(b12):
    b4 = BeautifulSoup(b12, 'lxml')
    b5 = []
    for i in b4.find_all('p'):
        try:
            if u"p-" in str(i['id']):
                b6 = str(i)[(str(i).find(">") + 1):(str(i).find("</p>", str(i).find(">") + 1))]
                b6 = re.sub(r'<.*?>', '', str(b6))
                b6 = re.sub(r'\n', ' ', str(b6))
                b6 = re.sub(r' +', ' ', str(b6))
                if len(b6) > 250:
                    b5.append(b6)
        except:
            pass
    a1 = 1
    b7 = []
    b8 = []
    for each in b4.find_all('li'):
        try:
            if 'last' in each['class'] and u'name' in str(each):
                b9 = each.find_all('a')[0].string
                b8.append(b9)
            elif 'aff' in each['class']:
                b10 = str(each.find_all('b10')[0])
                b10 = re.sub(r'<.*?>', '', str(b10))
                b10 = re.sub(r' +', ' ', str(b10))
                b10 = re.sub(r'\n', '', str(b10))
                if re.findall('[a-z]', b10[0]):
                    b10 = b10[1:]
                b10 = (str(a1) + "\t" + b10 + "\n")
                b7.append(b10)
                a1 += 1
        except:
            pass
    if len(b5) > 2:
        print("Content error")
        b5 = []
        b7 = []
        b8 = []
    return ''.join(b5), ''.join(b8), ''.join(b7)
def fonk3(vol, page):
    b11 = f"http:
    b12 = fonk1(b11)
    b6, b9, b10 = fonk2(b12)
    with open(f"{vol}-b6.csv", 'a', b3 = 'utf-8') as f1:
        with open(f"{vol}-b9.csv", 'a', b3 = 'utf-8') as f2:
            with open(f"{vol}-b10.csv", 'a', b3 = 'utf-8') as f3:
                if b6 and b6[-1] != "\n":
                    b6 += "\n"
                if b9 and b9[-1] != "\n":
                    b9 += "\n"
                if b10 and b10[-1] != "\n":
                    b10 += "\n"
                f1.write(f">{page}\n{b6}")
                f2.write(f">{page}\n{b9}")
                f3.write(f">{page}\n{b10}")
def fonk4(issue_number):
    return [1, 2, 3, 4, 5]
if b13 = = "__main__":
    for iss in range(1, 12):
        b14 = fonk4(iss)
        print(f"vol: {iss}")
        for page in b14:
            print(page)
            try:
                fonk3(iss, page)
            except Exception as e:
                print(e)