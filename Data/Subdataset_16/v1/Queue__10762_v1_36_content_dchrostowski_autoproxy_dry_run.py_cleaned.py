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
b4 = {k: 0 for k in b2}
b5 = {k: 0 for k in b2}
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
        if t.is_alive():
            a1 += 1
    return a1
def fonk3():
    print(threading.current_thread().getName(), "starting")
    time.sleep(random.randint(1, 10))
    b6 = ProxyManager()
    for _ in range(5):
        b7 = random.choice(b2)
        print(threading.current_thread().getName(), "crawling %s" % b7)
        b8 = b6.get_proxy(b7)
        time.sleep(random.randint(1, 12))
        b9 = random.choice(b3)
        print(threading.current_thread().getName(), "crawl b9 = %s" % b9)
        if b9:
            b4[b7] += 1
        else:
            b5[b7] += 1
        b8.callback(b9 = b9)
        time.sleep(random.randint(1, 6))
    print(threading.current_thread().getName(), "stopping")
def fonk4():
    b10 = []
    for i in range(5):
        b11 = "worker_%s" % i
        b12 = threading.Thread(name=b11, target=worker)
        b10.append(b12)
    return b10
b10 = fonk4()
def fonk5():
    print(threading.current_thread().getName(), 'Starting daemon.')
    for w in b10:
        w.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    b13 = StorageManager()
    b13.sync_to_db()
    return fonk1()
b14 = threading.Thread(name='daemon', target=daemon)
b14.setDaemon(True)
b14.start()