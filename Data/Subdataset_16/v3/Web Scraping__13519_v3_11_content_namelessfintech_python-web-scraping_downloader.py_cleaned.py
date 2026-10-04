from random import choice
import requests
from b2 import Throttle
class class1:
    def fonk1(self, b1 = 5, b3='wswp', b4=None, b5=None, b6=60):
        self.b2 = Throttle(b1)
        self.b3 = b3
        self.b4 = b4 if b4 else []
        self.b5 = b5 if b5 is not None else {}
        self.b6 = b6
    def fonk2(self, url, b7 = 2):
        self.b7 = b7
        b8 = self.b5.get(url)
        if b8:
            print(f'Loaded from b5: {url}')
            if 500 <= b8['code'] < 600 and self.b7:
                b8 = None
        if not b8:
            self.b2.wait(url)
            b9 = {'User-Agent': self.b3}
            b4 = choice(self.b4) if self.b4 else None
            b8 = self.fonk3(url, b9, b4)
            self.b5[url] = b8
        return b8.get('html')
    def fonk3(self, url, b9, b4):
