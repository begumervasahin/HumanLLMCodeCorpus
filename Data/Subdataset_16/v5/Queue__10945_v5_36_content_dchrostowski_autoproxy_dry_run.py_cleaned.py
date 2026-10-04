import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
b1 = Redis(**configuration.redis_config)
b1.flushall()
b2 = [
    'https:
    'http:
    'http:
    'http:
    'http:
    'http:
    'http:
]
b3 = [True, False]
b4 = {site: 0 for site in b2}
b5 = {site: 0 for site in b2}
def fonk1():
    print("--------------------------------------")
    print("Successes:")
    print(b4)
    print("--------------------------------------")
    print("Failures:")
    print(b5)
    print("--------------------------------------")
def fonk2():
    a1 = 0
    for t in threading.enumerate():
        print(t)
        if t.is_alive():
            a1 += 1
    return a1
def fonk3():
    print(f"{threading.current_thread().getName()} starting")
    time.sleep(random.randint(1, 10))
    b6 = ProxyManager()
    for _ in range(5):
        b7 = random.choice(b2)
        print(f"{threading.current_thread().getName()} crawling {b7}")
        b8 = b6.get_proxy(b7)
        time.sleep(random.randint(1, 12))
        b9 = random.choice(b3)
        print(f"{threading.current_thread().getName()} crawl b9 = {b9}")
        if b9:
            b4[b7] += 1
        else:
            b5[b7] += 1
        b8.callback(b9 = b9)
        time.sleep(random.randint(1, 6))
    print(f"{threading.current_thread().getName()} stopping")
def fonk4(b10 = 5):
    b11 = []
    for i in range(b10):
        b12 = f"worker_{i}"
        b13 = threading.Thread(name=b12, target=worker)
        b11.append(b13)
    return b11
def fonk5():
    print(f"{threading.current_thread().getName()} starting daemon.")
    for w in b11:
        w.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    b14 = StorageManager()
    b14.sync_to_db()
    fonk1()
b11 = fonk4()
b15 = threading.Thread(name='daemon', target=daemon)
b15.setDaemon(True)
b15.start()