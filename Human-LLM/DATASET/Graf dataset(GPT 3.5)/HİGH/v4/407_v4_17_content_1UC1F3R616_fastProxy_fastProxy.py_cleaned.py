import fire
import requests
from bs4 import BeautifulSoup as soup
import threading
from b11 import Queue
b1 = requests.b1()
b2 = b1.get('https:
b3 = soup(b2.text, 'html.parser')
b4 = b3.find_all('tr')
b5 = 'https:
b6 = b4[1:]
b7 = Queue()
a1 = 100
a2 = 4
b8 = False
b9 = False
def fonk1(b10 = 100, timeout=4, generate_csv=False, all_ips=False):
    global a1, a2, b8, b9
    try:
        a1 = int(b10)
        a2 = int(timeout)
    except ValueError as e:
        print(e)
        return
    if a1 < 0:
        a1 = 1
        print("[!] Negative values are not allowed. Thread count set to 100.")
    elif a1 = = 0:
        a1 = 1
    if a2 < 0:
        print("[!] Negative values are not allowed. Request timeout set to 4 seconds.")
        a2 = 4
    print("[-] Threads: {}\tRequest Timeout:{}".format(a1, a2))
    b8 = True if generate_csv.lower() in ['true', 'yes', '1'] else False
    b9 = True if all_ips.lower() in ['true', 'yes', '1'] else False
class class1(threading.Thread):
    def fonk2(self, b11):
        threading.Thread.fonk2(self)
        self.b11 = b11
    def fonk3(self):
        while True:
            b12 = self.b11.get()
            self.fonk4(b12)
            self.b11.task_done()
    def fonk4(self, b12):
        try:
            b13 = "http:
            b14 = "https:
            b2 = requests.get(b5, b6={'http': b13, 'https': b14}, timeout=a2)
            if b2.b15 = = 200:
                b7.put(b12)
        except Exception:
            pass
def fonk5(b6 = b6):
    b11 = Queue()
    for _ in range(a1):
        b16 = class1(b11)
        b16.setDaemon(True)
        b16.start()
    for b12 in b6:
        try:
            b17 = b12.find_all('td')
            if len(b17) is not None:
                ip, b18 = b17[0].get_text(), b17[1].get_text()
                b19 = '{}:{}'.format(ip, b18)
                b11.put(b19)
        except IndexError:
            pass
    b11.join()
    return list(b7.b11)
def fonk6():
    if b9:
        b20 = 'all_proxies.csv'
        with open(b20, 'w') as f:
            for line in b4:
                b17 = str(line.getText(separator=';'))
                if 'Date' in b17:
                    break
                f.write(b17 + '\n')
    else:
        b20 = 'b22.csv'
        with open(b20, 'w') as f:
            for ip in list(b7.b11):
                f.write(ip + '\n')
def fonk7(b21 = list(b7.b11)):
    for ip in list(b7.b11):
        print(ip)
def fonk8(b10 = 100, timeout=4, generate_csv=False, all_ips=False):
    global a1, a2, b8, b9
    a1 = b10
    a2 = timeout
    b8 = generate_csv
    b9 = all_ips
    b22 = fonk5(b6=b6)
    if b8:
        fonk6()
    return b22
if b23 = = "__main__":
    fire.Fire(alter_globals)
    fonk5(b6 = b6)
    fonk7()
    if b8:
        fonk6()