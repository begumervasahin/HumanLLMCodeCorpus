import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
redis = Redis(**configuration.redis_config)
redis.flushall()
test_sites = [
    'https:
    'http:
    'http:
    'http:
    'http:
    'http:
    'http:
]
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
    running = 0
    for t in threading.enumerate():
        print(t)
        if t.is_alive():
            running += 1
    return running
def worker():
    print(f"{threading.current_thread().getName()} starting")
    time.sleep(random.randint(1, 10))
    pm = ProxyManager()
    for _ in range(5):
        url = random.choice(test_sites)
        print(f"{threading.current_thread().getName()} crawling {url}")
        proxy = pm.get_proxy(url)
        time.sleep(random.randint(1, 12))
        success = random.choice(crawl_statuses)
        print(f"{threading.current_thread().getName()} crawl success={success}")
        if success:
            successful[url] += 1
        else:
            failures[url] += 1
        proxy.callback(success=success)
        time.sleep(random.randint(1, 6))
    print(f"{threading.current_thread().getName()} stopping")
def make_workers():
    workers = []
    for i in range(5):
        worker_name = f"worker_{i}"
        wkr = threading.Thread(name=worker_name, target=worker)
        workers.append(wkr)
    return workers
workers = make_workers()
def daemon():
    print(f"{threading.current_thread().getName()} starting daemon.")
    for w in workers:
        w.start()
    time.sleep(15)
    while True:
        scoreboard()
        if get_running_threads() == 1:
            break
        time.sleep(5)
    sm = StorageManager()
    sm.sync_to_db()
    return scoreboard()
dmn = threading.Thread(name='daemon', target=daemon)
dmn.setDaemon = True
dmn.start()