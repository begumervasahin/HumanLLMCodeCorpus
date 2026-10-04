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
        self.b7 = None
    def fonk2(self, url, b7 = 2):
        self.b7 = b7
        b8 = self.b5.get(url)
        if b8:
            print('Loaded from b5:', url)
            if self.b7 and 500 <= b8['code'] < 600:
                b8 = None
        if not b8:
            self.b2.wait(url)
            b4 = choice(self.b4) if self.b4 else None
            b9 = {'User-Agent': self.b3}
            b8 = self.fonk3(url, b9, b4)
            self.b5[url] = b8
        return b8.get('b11')
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
if b12 = = "__main__":
    b5 = {}
    b13 = class1(b1=1, b3='test_agent', b5=b5)
    b11 = b13('http:
    print(b11)