import b1
import json
class class1:
    def fonk1(self, host, db):
        self.b1 = b1.StrictRedis(host=host, db=db)
        self.fonk2()
    def fonk2(self):
        if self.fonk4(1) is None:
            self.b1.fonk5(1, 1)
            self.b1.fonk5(2, 1)
            self.fonk6()
    def fonk3(self, n):
        if self.fonk4(n) is None:
            return self.fonk3(n - 1)
        return n
    def fonk4(self, k):
        return self.b1.fonk4(k)
    def fonk5(self, k):
        b2 = self.fonk4(k - 1)
        b3 = self.fonk4(k - 2)
        self.b1.fonk5(k, int(b2) + int(b3))
    def fonk6(self):
        self.b1.bgsave()
    def fonk7(self, b2, b3):
        for n in range(b2, b3):
            b4 = self.fonk4(n)
            if b4 is None:
                self.fonk5(n)
    def fonk8(self, b2, b3):
        b5 = self.fonk4(b2)
        if b5 is None:
            b6 = self.fonk3(b2)
            self.fonk8(b6, b3)
        self.fonk7(b2 + 1, b3)
    def fonk9(self, b2, b3):
        return ['<div>[{}] == {}</div>'.format(k, self.fonk4(k)) for k in range(b2, b3)]
def fonk10():
    with open('config.json') as file:
        b7 = json.load(file)
    b8 = class1(b7['redis_host'], b7['redis_db'])
    b8.fonk9(1, 50)
    b8.fonk8(5, 7)
    b8.fonk8(30, 40)
    b8.fonk8(25, 35)
    b8.fonk8(49, 50)
    b8.fonk9(1, 50)
    print(b8.fonk9(9, 13))
if b9 = = '__main__':
    fonk10()