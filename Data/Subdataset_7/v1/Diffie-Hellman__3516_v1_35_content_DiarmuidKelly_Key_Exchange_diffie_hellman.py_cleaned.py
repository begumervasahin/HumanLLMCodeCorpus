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
    print('Private Key a1:', a1)
    print('Private Key a2:', a2)
    print('Verification Circle b3:', b3)
    b4 = class1(a1, a3, b3)
    b5 = class1(a2, a3, b3)
    b6 = b4.fonk2()
    b7 = b5.fonk2()
    print('Private a1 and Public:', b6)
    print('Private a2 and Public:', b7)
    b8 = b4.fonk3(b7)
    b9 = b5.fonk3(b6)
    print('Combined b8:', b8)
    print('Combined b9:', b9)
if b10 = = '__main__':
    fonk4()