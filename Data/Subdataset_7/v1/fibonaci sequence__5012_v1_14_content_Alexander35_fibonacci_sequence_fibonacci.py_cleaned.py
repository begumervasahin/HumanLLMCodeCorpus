import b1
import json
class class1():
    def fonk1(self, host, db):
        self.b1 = b1.StrictRedis(host=host, db=db)
        if self.fonk3(1) is None:
            self.b1.fonk4(1, 1)
            self.b1.fonk4(2, 1)
            self.fonk5()
    def fonk2(self, n):
        if self.fonk3(n) is None:
            return self.fonk2(n - 1)
        return n
    def fonk3(self, k):
        return self.b1.fonk3(k)
    def fonk4(self, k):
        b2 = self.fonk3(k - 1)
        b3 = self.fonk3(k - 2)
        self.b1.fonk4(k, int(b2) + int(b3))
    def fonk5(self):
        self.b1.bgsave()
    def fonk6(self, b2, b3):
        for n in range(b2, b3):
            b4 = self.fonk3(n)
            if b4 is None:
                self.fonk4(n)
    def fonk7(self, b2, b3):
        b5 = self.fonk3(b2)
        if b5 is None:
            b6 = self.fonk2(b2)
            self.fonk7(b6, b3)
        self.fonk6(b2 + 1, b3)
    def fonk8(self, b2, b3):
        return ['<div>[{}] == {}</div>'.format(k, self.fonk3(k)) for k in range(b2, b3)]
def fonk9():
    with open('config.json') as file:
        b7 = json.load(file)
    b8 = class1(b7['redis_host'], b7['redis_db'])
    b8.fonk8(1, 50)
    b8.fonk7(5, 7)
    b8.fonk7(30, 40)
    b8.fonk7(25, 35)
    b8.fonk7(49, 50)
    b8.fonk8(1, 50)
    print(b8.fonk8(9, 13))
if b9 = = '__main__':
    fonk9()