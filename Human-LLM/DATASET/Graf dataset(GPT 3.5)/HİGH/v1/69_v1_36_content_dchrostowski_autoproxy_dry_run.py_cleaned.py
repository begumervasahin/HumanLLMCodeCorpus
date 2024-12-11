import random
import time
import threading
b1 = ['https:
b2 = [True, False]
b3 = {k: 0 for k in b1}
b4 = {k: 0 for k in b1}
def fonk1():
    print("--------------------------------------")
    print("successes:")
    print(b3)
    print("--------------------------------------")
    print("b4:")
    print(b4)
    print("--------------------------------------")
def fonk2():
    a1 = 0
    for t in threading.enumerate():
        print(t)
        if t.isAlive():
            a1 += 1
    return a1
def fonk3():
    print(threading.currentThread().getName(), "starting")
    time.sleep(random.randint(1, 10))
    for i in range(5):
        b5 = random.choice(b1)
        print(threading.currentThread().getName(), "crawling %s" % b5)
        b6 = random.choice(b2)
        print(threading.currentThread().getName(), "crawl b6 = %s" % b6)
        if b6:
            b3[b5] += 1
        else:
            b4[b5] += 1
        time.sleep(random.randint(1, 12))
        time.sleep(random.randint(1, 6))
    print(threading.currentThread().getName(), "stopping")
def fonk4():
    b7 = []
    for i in range(5):
        b8 = "worker_%s" % i
        b9 = threading.Thread(name=b8, target=worker)
        b7.append(b9)
    return b7
b7 = fonk4()
def fonk5():
    print(threading.currentThread().getName(), 'Starting daemon.')
    for w in b7:
        w.start()
    time.sleep(15)
    while True:
        fonk1()
        if fonk2() == 1:
            break
        time.sleep(5)
    print(threading.currentThread().getName(), 'Stopping daemon.')
b10 = threading.Thread(name='daemon', target=daemon)
b10.b11 = True
b10.start()