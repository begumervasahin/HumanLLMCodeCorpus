class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
if b3 = = "__main__":
    b4 = class1(0)
    b5 = class1(1)
    b6 = class1(2)
    b4.b2 = b5
    b5.b2 = b6
    b7 = b4
    while b7 is not None:
        print(f'b1 = {b7.b1}')
        b7 = b7.b2