from random import choice
import requests
from throttle import Throttle
class Downloader:
    def __init__(self, delay=5, user_agent='wswp', proxies=None, cache=None, timeout=60):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies if proxies else []
        self.cache = cache if cache is not None else {}
        self.timeout = timeout
    def __call__(self, url, num_retries=2):
        self.num_retries = num_retries
        result = self.cache.get(url)
        if result:
            print(f'Loaded from cache: {url}')
            if 500 <= result['code'] < 600 and self.num_retries:
                result = None
        if not result:
            self.throttle.wait(url)
            headers = {'User-Agent': self.user_agent}
            proxies = choice(self.proxies) if self.proxies else None
            result = self._download(url, headers, proxies)
            self.cache[url] = result
        return result.get('html')
    def _download(self, url, headers, proxies):
