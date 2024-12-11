import requests
from bs4 import BeautifulSoup as soup
import threading
from b12 import Queue
import fire
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
def fonk1(b10 = 100, b11=4, generate_csv=False, fetch_all_ips=False):
    global a1, a2, b8, b9
    try:
        b10 = int(b10)
        b11 = int(b11)
    except ValueError as e:
        print("Invalid input:", e)
        return
    if b10 <= 0:
        a1 = 1
        print("[!] Negative Values are not Entertained")
        print("[*] Thread Count Set to 100")
    else:
        a1 = b10
    if b11 <= 0:
        print("[!] Negative Values are not Entertained")
        print("[*] Request Timeout Set to 4 sec")
    else:
        a2 = b11
    print("[-] Threads: {}\tRequest Timeout:{}".format(a1, a2))
    b8 = str(generate_csv).lower() in ['true', 'yes', '1']
    b9 = str(fetch_all_ips).lower() in ['true', 'yes', '1']
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
            b2 = requests.get(b5, b6={'http': b14, 'https': b15}, timeout=a2)
            if b2.b16 = = 200:
                b7.put(b13)
        except Exception as e:
            pass
def fonk5(b6):
    b12 = Queue()
    for _ in range(a1):
        b17 = class1(b12)
        b17.setDaemon(True)
        b17.start()
    for b13 in b6:
        try:
            b18 = b13.find_all('td')
            if b18:
                ip, b19 = b18[0].get_text(), b18[1].get_text()
                b20 = '{}:{}'.format(ip, b19)
                b12.put(b20)
        except Exception as e:
            print('[!] ' + str(e))
    b12.join()
    return list(b7.b12)
def fonk6():
    if b9:
        b21 = 'all_proxies.csv'
        with open(b21, 'w') as f:
            for line in b4:
                b18 = str(line.getText(separator=';'))
                if 'Date' in b18:
                    break
                f.write(b18 + '\n')
    else:
        b21 = 'b22.csv'
        with open(b21, 'w') as f:
            for ip in list(b7.b12):
                f.write(ip + '\n')
    print(f"CSV file '{b21}' generated successfully!")
def fonk7():
    for ip in list(b7.b12):
        print(ip)
def fonk8(b10 = 100, b11=4, generate_csv=False, fetch_all_ips=False):
    fonk1(b10, b11, generate_csv, fetch_all_ips)
    b22 = fonk5(b6)
    if b8:
        fonk6()
    return b22
if b23 = = "__main__":
    fire.Fire(alter_globals)
    fonk5(b6)
    fonk7()
    if b8:
        fonk6()