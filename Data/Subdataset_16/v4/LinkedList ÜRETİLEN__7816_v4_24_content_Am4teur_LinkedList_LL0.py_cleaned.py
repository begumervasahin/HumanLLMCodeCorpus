class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
def fonk2():
    b3 = class1(0)
    b3.b2 = class1(1)
    b3.b2.b2 = class1(2)
    b4 = b3
    while b4:
        print(f'b1 = {b4.b1}')
        b4 = b4.b2
if b5 = = "__main__":
    fonk2()