from random import choice
import requests
from b3 import Throttle
class class1:
    def fonk1(self, b1 = 5, b4='wswp', b5=None, b6={},
                 b2 = 60):
        self.b3 = Throttle(b1)
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = None
        self.b2 = b2
    def fonk2(self, url, b7 = 2):
        self.b7 = b7
        try:
            b8 = self.b6[url]
            print('Loaded from b6:', url)
        except KeyError:
            b8 = None
        if b8 and self.b7 and 500 <= b8['code'] < 600:
            b8 = None
        if b8 is None:
            self.b3.wait(url)
            b5 = choice(self.b5) if self.b5 else None
            b9 = {'User-Agent': self.b4}
            b8 = self.fonk3(url, b9, b5)
            self.b6[url] = b8
        return b8['b11']
    def fonk3(self, url, b9, b5):
        print('Downloading:', url)
        try:
            b10 = requests.get(url, b9=b9, b5=b5,
                                b2 = self.b2)
            b11 = b10.text
            if b10.status_code >= 400:
                print('Download error:', b10.text)
                b11 = None
                if self.b7 and 500 <= b10.status_code < 600:
                    self.b7 -= 1
                    return self.fonk3(url, b9, b5)
        except requests.exceptions.RequestException as e:
            print('Download error:', e)
            return {'b11': None, 'code': 500}
        return {'b11': b11, 'code': b10.status_code}