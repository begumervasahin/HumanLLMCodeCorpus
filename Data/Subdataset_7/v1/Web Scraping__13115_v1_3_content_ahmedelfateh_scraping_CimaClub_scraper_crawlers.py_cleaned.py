import threading
from b6 import Queue
from workfiles.createdir import *
from workfiles.linkgetter import *
from workfiles.crawler import *
b1 = 'CimaClub'
b2 = 'http:
b3 = get_domain_name(b2)
b4 = b1 + '/getURL.txt'
b5 = b1 + '/setURL.tex'
a1 = 8
b6 = Queue()
def fonk1():
    b7 = file_to_set(b4)
    if len(b7) > 0:
        print(str(len(b7)) + " Links in the Queue")
        fonk2()
def fonk2():
    for link in file_to_set(b4):
        b6.put(link)
    b6.join()
    fonk1()
def fonk3():
    for _ in range(a1):
        b8 = threading.Thread(target=work)
        b8.b9 = True
        b8.start()
def fonk4():
    while True:
        b10 = b6.get()
        Crawler.crawl_page(threading.current_thread().name, b10)
        b6.task_done()
if b11 = = "__main__":
    Crawler(b1, b2, b3)
    fonk3()
    fonk1()