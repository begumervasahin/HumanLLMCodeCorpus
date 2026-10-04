import requests
from random import choice
from b2 import Throttle
class class1:
    def fonk1(self, b1 = 5, b3='wswp', b4=None, b5=None, b6=60):
        self.b2 = Throttle(b1)
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5 if b5 is not None else {}
        self.b6 = b6
    def fonk2(self, url, b7 = 2):
        self.b7 = b7
        b8 = self.fonk3(url)
        if b8 is None or (self.fonk4(b8) and self.b7):
            self.b2.wait(url)
            b4 = self.fonk5()
            b9 = self.fonk6()
            b8 = self.fonk7(url, b9, b4)
            self.b5[url] = b8
        return b8['b11']
    def fonk3(self, url):
        try:
            b8 = self.b5[url]
            print('Loaded from b5:', url)
            return b8
        except KeyError:
            return None
    def fonk4(self, b8):
        return 500 <= b8['code'] < 600
    def fonk5(self):
        return choice(self.b4) if self.b4 else None
    def fonk6(self):
        return {'User-Agent': self.b3}
    def fonk7(self, url, b9, b4):
        print('Downloading:', url)
        try:
            b10 = requests.get(url, b9=b9, b4=b4, b6=self.b6)
            b11 = b10.text
            if b10.status_code >= 400:
                print('Download error:', b10.text)
                b11 = None
                if self.fonk4({'code': b10.status_code}):
                    self.b7 -= 1
                    return self.fonk7(url, b9, b4)
        except requests.exceptions.RequestException as e:
            print('Download error:', e)
            return {'b11': None, 'code': 500}
        return {'b11': b11, 'code': b10.status_code}