import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.b16 import StorageManager, Redis
from scrapy_autoproxy.b8 import ProxyManager
b1 = Redis(**configuration.redis_config)
b1.flushall()
b2 = ['https:
'http:
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
    b6 = sum(1 for t in threading.enumerate() if t.is_alive())
    return b6
def fonk3():
    b7 = threading.currentThread().getName()
    print(b7, "starting")
    time.sleep(random.randint(1, 10))
    b8 = ProxyManager()
    for _ in range(5):
        b9 = random.choice(b2)
        print(b7, "crawling %s" % b9)
        b10 = b8.get_proxy(b9)
        time.sleep(random.randint(1, 12))
        b11 = random.choice(b3)
        print(b7, "crawl b11 = %s" % b11)
        if b11:
            b4[b9] += 1
        else:
            b5[b9] += 1
        b10.callback(b11 = b11)
        time.sleep(random.randint(1, 6))
    print(b7, "stopping")
def fonk4():
    b12 = []
    for i in range(5):
        b13 = "worker_%s" % i
        b14 = threading.Thread(name=b13, target=worker)
        b12.append(b14)
    return b12
b12 = fonk4()
def fonk5():
    b15 = threading.currentThread().getName()
    print(b15, 'Starting daemon.')
    for b14 in b12:
        b14.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    b16 = StorageManager()
    b16.sync_to_db()
    return fonk1()
b17 = threading.Thread(name='daemon', target=daemon)
b17.b18 = True
b17.start()