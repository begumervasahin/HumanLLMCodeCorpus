import b1
import json
class class1:
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
        b2 = int(self.fonk3(k - 1))
        b3 = int(self.fonk3(k - 2))
        self.b1.fonk4(k, b2 + b3)
    def fonk5(self):
        self.b1.bgsave()
    def fonk6(self, start, end):
        for n in range(start, end):
            if self.fonk3(n) is None:
                self.fonk4(n)
    def fonk7(self, start, end):
        if self.fonk3(start) is None:
            b4 = self.fonk2(start)
            self.fonk7(b4, end)
        self.fonk6(start + 1, end)
    def fonk8(self, start, end):
        return [f'<div>[{k}] == {self.fonk3(k)}</div>' for k in range(start, end)]
def fonk9():
    with open('config.json') as file:
        b5 = json.load(file)
    b6 = class1(b5['redis_host'], b5['redis_db'])
    print(b6.fonk8(1, 50))
    b6.fonk7(5, 7)
    b6.fonk7(30, 40)
    b6.fonk7(25, 35)
    b6.fonk7(49, 50)
    print(b6.fonk8(1, 50))
    print(b6.fonk8(9, 13))
if b7 = = '__main__':
    fonk9()