import random
import time
import threading
test_sites = ['https:
crawl_statuses = [True, False]
successful = {site: 0 for site in test_sites}
failures = {site: 0 for site in test_sites}
def display_scoreboard():
    print("--------------------------------------")
    print("Successes:")
    print(successful)
    print("--------------------------------------")
    print("Failures:")
    print(failures)
    print("--------------------------------------")
def count_running_threads():
    return sum(1 for t in threading.enumerate() if t.is_alive())
def crawl_worker():
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
def create_and_start_workers():
    workers = []
    for i in range(5):
        worker_name = "worker_%s" % i
        worker_thread = threading.Thread(name=worker_name, target=crawl_worker)
        workers.append(worker_thread)
        worker_thread.start()
    return workers
workers = create_and_start_workers()
def manage_workers():
    print(threading.currentThread().getName(), 'Starting daemon.')
    time.sleep(15)
    while True:
        display_scoreboard()
        if count_running_threads() == 1:
            break
        time.sleep(5)
    print(threading.currentThread().getName(), 'Stopping daemon.')
daemon_thread = threading.Thread(name='daemon', target=manage_workers)
daemon_thread.daemon = True
daemon_thread.start()