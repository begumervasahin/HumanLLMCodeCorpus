import random
import time
import threading
b1 = ['https:
b2 = [True, False]
b3 = {site: 0 for site in b1}
b4 = {site: 0 for site in b1}
def fonk1():
    print("--------------------------------------")
    print("Successes:")
    print(b3)
    print("--------------------------------------")
    print("Failures:")
    print(b4)
    print("--------------------------------------")
def fonk2():
    return sum(1 for t in threading.enumerate() if t.is_alive())
def fonk3():
    print(threading.currentThread().getName(), "starting")
    time.sleep(random.randint(1, 10))
    for _ in range(5):
        b5 = random.choice(b1)
        print(threading.currentThread().getName(), "crawling %s" % b5)
        b6 = random.choice(b2)
        print(threading.currentThread().getName(), "crawl b6 = %s" % b6)
        if b6:
            b3[b5] += 1
        else:
            b4[b5] += 1
        time.sleep(random.randint(1, 12))
    print(threading.currentThread().getName(), "stopping")
def fonk4():
    b7 = []
    for i in range(5):
        b8 = "worker_%s" % i
        b9 = threading.Thread(name=b8, target=crawl_worker)
        b7.append(b9)
        b9.start()
    return b7
b7 = fonk4()
def fonk5():
    print(threading.currentThread().getName(), 'Starting b11.')
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    print(threading.currentThread().getName(), 'Stopping b11.')
b10 = threading.Thread(name='b11', target=manage_workers)
b10.b11 = True
b10.start()