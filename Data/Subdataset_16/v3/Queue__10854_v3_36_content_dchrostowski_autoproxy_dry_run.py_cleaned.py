import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
class class1:
    def fonk1(self, b3, b4, b1 = 5):
        self.b2 = Redis(**configuration.redis_config)
        self.b2.flushall()
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = {site: 0 for site in self.b3}
        self.b6 = {site: 0 for site in self.b3}
        self.b7 = self.fonk5()
    def fonk2(self):
        print("--------------------------------------")
        print("Successes:")
        for site, count in self.b5.items():
            print(f"{site}: {count}")
        print("--------------------------------------")
        print("Failures:")
        for site, count in self.b6.items():
            print(f"{site}: {count}")
        print("--------------------------------------")
    def fonk3(self):
        return sum(1 for t in threading.enumerate() if t.is_alive())
    def fonk4(self):
        b8 = threading.current_thread().getName()
        print(f"{b8} starting")
        time.sleep(random.randint(1, 10))
        b9 = ProxyManager()
        for _ in range(5):
            b10 = random.choice(self.b3)
            print(f"{b8} crawling {b10}")
            b11 = b9.get_proxy(b10)
            time.sleep(random.randint(1, 12))
            b12 = random.choice(self.b4)
            print(f"{b8} crawl b12 = {b12}")
            if b12:
                self.b5[b10] += 1
            else:
                self.b6[b10] += 1
            b11.callback(b12 = b12)
            time.sleep(random.randint(1, 6))
        print(f"{b8} stopping")
    def fonk5(self):
        b7 = []
        for i in range(self.b1):
            b13 = f"worker_{i}"
            b14 = threading.Thread(name=b13, target=self._worker)
            b7.append(b14)
        return b7
    def fonk6(self):
        print(threading.current_thread().getName(), 'Starting daemon.')
        for b14 in self.b7:
            b14.fonk7()
        time.sleep(15)
        while True:
            self.fonk2()
            if self.fonk3() == 1:
                break
            time.sleep(5)
        b15 = StorageManager()
        b15.sync_to_db()
        self.fonk2()
    def fonk7(self):
        b16 = threading.Thread(name='daemon', target=self._daemon)
        b16.setDaemon(True)
        b16.fonk7()
if b17 = = "__main__":
    b3 = [
        'https:
        'http:
        'http:
        'http:
        'http:
        'http:
        'http:
    ]
    b4 = [True, False]
    b18 = class1(b3, b4, b1=5)
    b18.fonk7()