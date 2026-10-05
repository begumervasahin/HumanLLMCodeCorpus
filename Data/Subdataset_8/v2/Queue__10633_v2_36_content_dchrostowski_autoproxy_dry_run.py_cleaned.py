import random
import time
import threading
test_sites = ['https:
crawl_statuses = [True, False]
successful = {site: 0 for site in test_sites}
failures = {site: 0 for site in test_sites}
def scoreboard():
    print("--------------------------------------")
    print("Successes:")
    print(successful)
    print("--------------------------------------")
    print("Failures:")
    print(failures)
    print("--------------------------------------")
def get_running_threads():
    running = sum(1 for t in threading.enumerate() if t.is_alive())
    return running
def worker():
    print(threading.currentThread().getName(), "starting")
    time.sleep(random.randint(1, 10))
    for _ in range(5):
        url = random.choice(test_sites)
        print(threading.currentThread().getName(), "crawling %s" % url)
        success = random.choice(crawl_statuses)
        print(threading.currentThread().getName(), "crawl success=%s" % success)
        if success:
            successful[url] += 1
        else:
            failures[url] += 1
        time.sleep(random.randint(1, 12))
    print(threading.currentThread().getName(), "stopping")
def make_workers():
    workers = []
    for i in range(5):
        worker_name = "worker_%s" % i
        wkr = threading.Thread(name=worker_name, target=worker)
        workers.append(wkr)
    return workers
workers = make_workers()
def daemon():
    print(threading.currentThread().getName(), 'Starting daemon.')
    for w in workers:
        w.start()
    time.sleep(15)
    while True:
        scoreboard()
        if get_running_threads() == 1:
            break
        time.sleep(5)
    print(threading.currentThread().getName(), 'Stopping daemon.')
dmn = threading.Thread(name='daemon', target=daemon)
dmn.daemon = True
dmn.start()