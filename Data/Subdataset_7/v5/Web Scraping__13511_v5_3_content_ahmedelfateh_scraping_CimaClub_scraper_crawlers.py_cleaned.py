import threading
from queue import Queue
from workfiles.createdir import create_project_directory, get_domain_name
from workfiles.linkgetter import file_to_set
from workfiles.b7 import Crawler
b1 = 'CimaClub'
b2 = 'http:
b3 = get_domain_name(b2)
b4 = f'{b1}/getURL.txt'
b5 = f'{b1}/setURL.tex'
a1 = 8
b6 = Queue()
create_project_directory(b1)
b7 = Crawler(b1, b2, b3)
def fonk1():
    b8 = file_to_set(b4)
    if b8:
        print(f"{len(b8)} links in the queue")
        fonk2()
def fonk2():
    for link in file_to_set(b4):
        b6.put(link)
        b6.join()
        fonk1()
def fonk3():
    for _ in range(a1):
        b9 = threading.Thread(target=work)
        b9.b10 = True
        b9.start()
def fonk4():
    while True:
        b11 = b6.get()
        Crawler.crawl_page(threading.current_thread().name, b11)
        b6.task_done()
fonk3()
fonk1()