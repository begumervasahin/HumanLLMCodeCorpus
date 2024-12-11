import fire
import requests
from bs4 import BeautifulSoup as soup
import threading
from b8 import Queue
b1 = 'https:
b2 = 'https:
a1 = 100
a2 = 4
b3 = []
b4 = Queue()
b5 = False
b6 = False
def fonk1(b7 = a1, timeout=a2, csv=False, all_ips=False):
    global a1, a2, b5, b6
    try:
        a1 = int(b7)
        a2 = int(timeout)
    except ValueError as e:
        print(e)
        return
    if a1 < 1:
        a1 = 1
        print("[!] Thread count cannot be less than 1. Defaulting to 1.")
    if a2 < 0:
        print("[!] Request timeout cannot be negative. Defaulting to 4 seconds.")
        a2 = 4
    print("[-] Threads: {}\tRequest Timeout: {}".format(a1, a2))
    b5 = csv.lower() in ['true', 'yes', '1']
    b6 = all_ips.lower() in ['true', 'yes', '1']
class class1(threading.Thread):
    def fonk2(self, b8):
        threading.Thread.fonk2(self)
        self.b8 = b8
    def fonk3(self):
        while True:
            b9 = self.b8.get()
            self.fonk4(b9)
            self.b8.task_done()
    def fonk4(self, b9):
        try:
            b10 = "http:
            b11 = "https:
            b12 = requests.get(b2, b3={'http': b10, 'https': b11}, timeout=a2)
            if b12.b13 = = 200:
                b4.put(b9)
        except Exception:
            pass
def fonk5():
    global b3
    b14 = requests.b14()
    b12 = b14.get(b1)
    b15 = soup(b12.text, 'html.parser')
    b16 = b15.find_all('tr')
    b3 = b16[1:]
def fonk6():
    b8 = Queue()
    for _ in range(a1):
        b17 = class1(b8)
        b17.setDaemon(True)
        b17.start()
    for proxy_row in b3:
        try:
            ip, b18 = [data.text for data in proxy_row.find_all('td')[:2]]
            b19 = '{}:{}'.format(ip, b18)
            b8.put(b19)
        except Exception:
            pass
    b8.join()
def fonk7():
    b20 = 'all_proxies.csv' if b6 else 'working_ips.csv'
    with open(b20, 'w') as f:
        for proxy_row in b3:
            b21 = str(proxy_row.getText(separator=';'))
            if 'Date' in b21:
                break
            f.write(b21 + '\n')
def fonk8():
    for ip in list(b4.b8):
        print(ip)
def fonk9():
    fonk5()
    fonk6()
    fonk8()
    if b5:
        fonk7()
if b22 = = "__main__":
    fire.Fire(alter_globals)
    fonk9()