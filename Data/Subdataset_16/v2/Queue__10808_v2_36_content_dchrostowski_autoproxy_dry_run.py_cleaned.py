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
    for site, count in b4.items():
        print(f"{site}: {count}")
    print("--------------------------------------")
    print("Failures:")
    for site, count in b5.items():
        print(f"{site}: {count}")
    print("--------------------------------------")
def fonk2():
    return sum(1 for t in threading.enumerate() if t.is_alive())
def fonk3():
    b6 = threading.current_thread().getName()
    print(f"{b6} starting")
    time.sleep(random.randint(1, 10))
    b7 = ProxyManager()
    for _ in range(5):
        b8 = random.choice(b2)
        print(f"{b6} crawling {b8}")
        b9 = b7.get_proxy(b8)
        time.sleep(random.randint(1, 12))
        b10 = random.choice(b3)
        print(f"{b6} crawl b10 = {b10}")
        if b10:
            b4[b8] += 1
        else:
            b5[b8] += 1
        b9.callback(b10 = b10)
        time.sleep(random.randint(1, 6))
    print(f"{b6} stopping")
def fonk4(b11 = 5):
    b12 = []
    for i in range(b11):
        b13 = f"worker_{i}"
        b14 = threading.Thread(name=b13, target=worker)
        b12.append(b14)
    return b12
b12 = fonk4()
def fonk5():
    print(threading.current_thread().getName(), 'Starting daemon.')
    for b14 in b12:
        b14.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    b15 = StorageManager()
    b15.sync_to_db()
    fonk1()
b16 = threading.Thread(name='daemon', target=daemon)
b16.setDaemon(True)
b16.start()