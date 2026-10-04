import b1
import json
class class1:
    def fonk1(self, host, db):
        self.b1 = b1.StrictRedis(host=host, db=db)
        if not self.fonk2(1):
            self.b1.set(1, 1)
            self.b1.set(2, 1)
            self.fonk4()
    def fonk2(self, k):
        b2 = self.b1.get(k)
        return int(b2) if b2 else None
    def fonk3(self, k):
        b3 = self.fonk2(k - 1)
        b4 = self.fonk2(k - 2)
        self.b1.set(k, b3 + b4)
    def fonk4(self):
        self.b1.bgsave()
    def fonk5(self, n):
        if not self.fonk2(n):
            return self.fonk5(n - 1)
        return n
    def fonk6(self, start, end):
        for n in range(start, end):
            if not self.fonk2(n):
                self.fonk3(n)
    def fonk7(self, start, end):
        if not self.fonk2(start):
            b5 = self.fonk5(start)
            self.fonk7(b5, end)
        self.fonk6(start + 1, end)
    def fonk8(self, start, end):
        return [f'<div>[{k}] == {self.fonk2(k)}</div>' for k in range(start, end)]
def fonk9():
    with open('config.json') as file:
        b6 = json.load(file)
    b7 = class1(b6['redis_host'], b6['redis_db'])
    print('\n'.join(b7.fonk8(1, 50)))
    b7.fonk7(5, 7)
    b7.fonk7(30, 40)
    b7.fonk7(25, 35)
    b7.fonk7(49, 50)
    print('\n'.join(b7.fonk8(1, 50)))
    print('\n'.join(b7.fonk8(9, 13)))
if b8 = = '__main__':
    fonk9()