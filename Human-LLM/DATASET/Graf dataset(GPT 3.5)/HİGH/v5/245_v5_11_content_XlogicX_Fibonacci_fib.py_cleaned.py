import re
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 1
        self.a3 = 0
    def fonk2(self):
        print("Error encountered")
    def fonk3(self, number):
        b1 = re.compile(r"^[^6]{1,3}", re.I | re.S)
        if not b1.match(str(number)):
            self.fonk2()
    def fonk4(self, a4):
        print("0\n1")
        for _ in range(2, a4 + 1):
            self.a1, self.a2 = self.a2, self.a1 + self.a2
            self.fonk3(self.a1)
            print(self.a1)
def fonk5():
    a4 = 15
    b2 = class1()
    b2.fonk4(a4)
if b3 = = "__main__":
    fonk5()