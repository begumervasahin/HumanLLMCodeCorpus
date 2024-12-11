from bs4 import BeautifulSoup
import urllib2
import re
import sys
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
    b7 = []
    b8 = []
    for paragraph in b5.find_all('p'):
        try:
            if u"p-" in str(paragraph['id']):
                b9 = re.sub(r'<.*?>', '', str(paragraph)[(str(paragraph).find(">") + 1):(str(paragraph).find("</p>", str(paragraph).find(">") + 1))])
                b9 = re.sub(r'\n', ' ', str(b9))
                b9 = re.sub(r' +', ' ', str(b9))
                if len(b9) > 250:
                    b6.append(b9)
        except:
            pass
    a1 = 1
    for item in b5.find_all('li'):
        try:
            if 'last' in item['class'] and u'name' in str(item):
                b10 = item.find_all('a')[0].string
                b7.append(b10)
            elif 'aff' in item['class']:
                b11 = str(item.find_all('b11')[0])
                b11 = re.sub(r'<.*?>', '', str(b11))
                b11 = re.sub(r' +', ' ', str(b11))
                b11 = re.sub(r'\n', '', str(b11))
                if re.findall('[a-z]', b11[0]):
                    b11 = b11[1:]
                b11 = (str(a1) + "\t" + b11 + "\n")
                b8.append(b11)
                a1 += 1
        except:
            pass
    if len(b6) > 2:
        print("Content error")
        b6 = []
        b8 = []
        b7 = []
    return ''.join(b6), ''.join(b7), ''.join(b8)
def fonk3(vol, page):
    b12 = "http:
    b4 = fonk1(b12)
    b9, b10, b11 = fonk2(b4)
    with open(str(vol) + '-b9.csv', 'a') as f1, \
         open(str(vol) + '-b10.csv', 'a') as f2, \
         open(str(vol) + '-b11.csv', 'a') as f3:
        if b9[-1] != "\n":
            b9 = b9 + "\n"
        if b10[-1] != "\n":
            b10 = b10 + "\n"
        if b11[-1] != "\n":
            b11 = b11 + "\n"
        f1.write(">" + str(page) + "\n" + b9)
        f2.write(">" + str(page) + "\n" + b10)
        f3.write(">" + str(page) + "\n" + b11)
if b13 = = "__main__":
    for iss in range(1, 12):
        b14 = get_issues(iss)
        print("Volume: " + str(iss))
        for i in b14:
            print(i)
            try:
                fonk3(iss, i)
            except Exception as e:
                print(e)