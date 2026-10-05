import requests
from bs4 import BeautifulSoup as soup
import threading
from b12 import Queue
import fire
b1 = requests.session()
b2 = b1.get('https:
b3 = soup(b2.text, 'html.parser')
b4 = b3.find_all('tr')
b5 = 'https:
b6 = b3.find_all('tr')[1:]
b7 = Queue()
a1 = 100
a2 = 4
b8 = False
b9 = False
def fonk1(b10 = 100, b11=4, g=False, a=False):
    global a1, a2, b8, b9
    try:
        b10 = int(b10)
        b11 = int(b11)
    except Exception as e:
        print(e)
        return
    if b10 < 0:
        a1 = 1
        print("[!] Negative Values are not Entertained")
        print("[*] Thread Count Set to 100")
    elif b10 = = 0:
        a1 = 1
    if b11 < 0:
        print("[!] Negative Values are not Entertained")
        print("[*] Request Timeout Set to 4 sec")
    a1 = b10
    a2 = b11
    print("[-] Threads: {}\tRequest Timeout:{}".format(a1, a2))
    if g in ['True', 'true', True, 1, 'yes']:
        b8 = True
    if a in ['True', 'true', True, 1, 'yes']:
        b9 = True
class class1(threading.Thread):
    def fonk2(self, b12):
        threading.Thread.fonk2(self)
        self.b12 = b12
    def fonk3(self):
        while True:
            b13 = self.b12.get()
            self.fonk4(b13)
            self.b12.task_done()
    def fonk4(self, b13):
        try:
            b14 = "http:
            b15 = "https:
            b16 = requests.get(b5, b18={'http': b14, 'https': b15}, timeout=a2)
            if b16.b17 = = 200:
                b7.put(b13)
        except Exception as e:
            pass
def fonk5(b18 = b6):
    b12 = Queue()
    for i in range(a1):
        b11 = class1(b12)
        b11.setDaemon(True)
        b11.start()
    for b13 in b18:
        try:
            b19 = b13.find_all('td')
            if len(b19) != None:
                ip, b20 = b19[0].get_text(), b19[1].get_text()
                b21 = '{}:{}'.format(ip, b20)
                b12.put(b21)
        except IndexError:
            pass
        except Exception as e:
            print('[!] ' + str(e))
    b12.join()
    return list(b7.b12)
def fonk6():
    if b9:
        with open('all_proxies.csv', 'w') as f:
            for line in b4:
                b19 = str(line.getText(separator=';'))
                if 'Date' in b19:
                    break
                f.write(b19 + '\n')
    else:
        with open('b23.csv', 'w') as f:
            for ip in list(b7.b12):
                f.write(ip + '\n')
def fonk7(b22 = list(b7.b12)):
    for ip in list(b7.b12):
        print(ip)
def fonk8(b10 = 100, b11=4, g=False, a=False):
    global a1, a2, b8, b9
    a1 = b10
    a2 = b11
    b8 = g
    b9 = a
    b23 = fonk5(b18=b6)
    if b8:
        fonk6()
    return b23
if b24 = = "__main__":
    fire.Fire(alter_globals)
    fonk5(b18 = b6)
    fonk7()
    if b8:
        fonk6()