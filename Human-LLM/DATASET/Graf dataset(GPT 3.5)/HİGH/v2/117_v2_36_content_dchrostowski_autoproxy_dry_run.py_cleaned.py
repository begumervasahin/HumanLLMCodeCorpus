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
    b5 = sum(1 for t in threading.enumerate() if t.is_alive())
    return b5
def fonk3():
    print(threading.currentThread().getName(), "starting")
    time.sleep(random.randint(1, 10))
    for _ in range(5):
        b6 = random.choice(b1)
        print(threading.currentThread().getName(), "crawling %s" % b6)
        b7 = random.choice(b2)
        print(threading.currentThread().getName(), "crawl b7 = %s" % b7)
        if b7:
            b3[b6] += 1
        else:
            b4[b6] += 1
        time.sleep(random.randint(1, 12))
    print(threading.currentThread().getName(), "stopping")
def fonk4():
    b8 = []
    for i in range(5):
        b9 = "worker_%s" % i
        b10 = threading.Thread(name=b9, target=worker)
        b8.append(b10)
    return b8
b8 = fonk4()
def fonk5():
    print(threading.currentThread().getName(), 'Starting b12.')
    for w in b8:
        w.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    print(threading.currentThread().getName(), 'Stopping b12.')
b11 = threading.Thread(name='b12', target=b12)
b11.b12 = True
b11.start()