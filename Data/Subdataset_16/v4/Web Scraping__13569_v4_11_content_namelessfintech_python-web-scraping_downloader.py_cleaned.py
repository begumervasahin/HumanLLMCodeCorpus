import requests
from random import choice
from b2 import Throttle
class class1:
    def fonk1(self, b1 = 5, b3='wswp', b4=None, b5={}, b6=60):
        self.b2 = Throttle(b1)
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk2(self, url, b7 = 2):
        self.b7 = b7
        try:
            b8 = self.b5[url]
            print('Loaded from b5:', url)
        except KeyError:
            b8 = None
        if b8 and self.b7 and 500 <= b8['code'] < 600:
            b8 = None
        if b8 is None:
            self.b2.wait(url)
            b4 = choice(self.b4) if self.b4 else None
            b9 = {'User-Agent': self.b3}
            b8 = self.fonk3(url, b9, b4)
            self.b5[url] = b8
        return b8['b11']
    def fonk3(self, url, b9, b4):
        print('Downloading:', url)
        try:
            b10 = requests.get(url, b9=b9, b4=b4, b6=self.b6)
            b11 = b10.text
            if b10.status_code >= 400:
                print('Download error:', b10.text)
                b11 = None
                if self.b7 and 500 <= b10.status_code < 600:
                    self.b7 -= 1
                    return self.fonk3(url, b9, b4)
        except requests.exceptions.RequestException as e:
            print('Download error:', e)
            return {'b11': None, 'code': 500}
        return {'b11': b11, 'code': b10.status_code}