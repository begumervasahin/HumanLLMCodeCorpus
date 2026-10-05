from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
from IPython import embed
import random
import time
import threading
b1 = threading.currentThread()
b2 = Redis(**configuration.redis_config)
b2.flushall()
b3 = ['https:
b4 = [True,False]
b5 = {k: 0 for k in b3}
b6 = {k: 0 for k in b3 }
def fonk1():
    print("--------------------------------------")
    print("successes:")
    print(b5)
    print("--------------------------------------")
    print("b6:")
    print(b6)
    print("--------------------------------------")
def fonk2():
    a1 = 0
    for t in threading.enumerate():
        print(t)
        if t.isAlive():
            a1 +=1
    return a1
def fonk3():
    print(threading.currentThread().getName(), "starting")
    time.sleep(random.randint(1,10))
    b7 = ProxyManager()
    for i in range(5):
        b8 = random.choice(b3)
        print(threading.currentThread().getName(), "crawling %s" % b8)
        b9 = b7.get_proxy(b8)
        time.sleep(random.randint(1,12))
        b10 = random.choice(b4)
        print(threading.currentThread().getName(), "crawl b10 = %s" % b10)
        if b10:
            b5[b8] += 1
        else:
            b6[b8] +=1
        b9.callback(b10 = b10)
        time.sleep(random.randint(1,6))
    print(threading.currentThread().getName(), "stopping")
    return
def fonk4():
    b11 = []
    for i in range(5):
        b12 = "worker_%s" % i
        b13 = threading.Thread(name=b12, target=worker)
        b11.append(b13)
    return b11
b11 = fonk4()
def fonk5():
    print(threading.currentThread().getName(), 'Starting daemon.')
    for w in b11:
        w.start()
    time.sleep(15)
    while(True):
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    b14 = StorageManager()
    b14.sync_to_db()
    return fonk1()
b15 = threading.Thread(name='daemon', target=daemon)
b15.b16 = True
b15.start()