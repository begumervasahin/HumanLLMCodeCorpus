import re
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import logging
class Ingestion:
    def __init__(self, sitemap, regex, concurrency=20, proxy=None):
        self.regex = re.compile(regex)
        self.links = set()
        self.queue = Queue()
        self.queue.put(sitemap)
        self.thread_pool = ThreadPoolExecutor(max_workers=concurrency)
        self.user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
        self.proxy = {'https': proxy, 'http': proxy}
    def parser(self, response):
        raise NotImplementedError
    def _parser_callback(self, future):
        response = future.result()
        if response:
            self.parser(response)
    def _recursive_sitemap_parse(self):
        while not self.queue.empty():
            sitemap = self.queue.get_nowait()
            self.__parse_sitemap_xml(sitemap)
    def __parse_sitemap_xml(self, sitemap):
        try:
            response = requests.get(sitemap)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml-xml')
            raw_urls = soup.find_all('loc')
            for raw in raw_urls:
                url = raw.text
                if url.endswith('.xml'):
                    self.queue.put(url)
                elif re.match(self.regex, url):
                    self.links.add(url)
        except requests.RequestException as e:
            logging.warning(f"Exception retrieving sitemap: {sitemap}, Exception: {e}")
    def _get_response_object(self, url):
        try:
            response = requests.get(url, proxies=self.proxy, timeout=(30, 60))
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.warning(f"Request failed for {url}: {e}")
            return None
    def digest(self):
        self._recursive_sitemap_parse()
        for link in self.links:
            future = self.thread_pool.submit(self._get_response_object, link)
            future.add_done_callback(self._parser_callback)
class MyIngestion(Ingestion):
    def parser(self, response):
        print(f"Processing URL: {response.url}")
