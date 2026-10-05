class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return pow(self.b2, self.b1, self.b3)
    def fonk3(self, combined_key):
        return pow(combined_key, self.b1, self.b3)
def fonk4():
    b3 = 100000
    a1 = 3426158395
    a2 = 3479502846
    a3 = 6748390294
    print('Public Key:', a3)
    print('Private Key a:', a1)
    print('Private Key b:', a2)
    print('Verification Circle:', b3)
    b4 = class1(a1, a3, b3)
    b5 = class1(a2, a3, b3)
    b6 = b4.fonk2()
    b7 = b5.fonk2()
    print('Combined Key of Private a and Public:', b6)
    print('Combined Key of Private b and Public:', b7)
    b8 = b4.fonk3(b7)
    b9 = b5.fonk3(b6)
    print('Verification Result for Combined Key agb:', b8)
    print('Verification Result for Combined Key bga:', b9)
if b10 = = '__main__':
    fonk4()