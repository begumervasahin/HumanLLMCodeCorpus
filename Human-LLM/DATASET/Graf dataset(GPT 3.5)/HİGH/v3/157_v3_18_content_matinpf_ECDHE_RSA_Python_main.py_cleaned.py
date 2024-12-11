class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        pass
    def fonk3(self):
        pass
    def fonk4(self, data1, data2):
        pass
    def fonk5(self, data_hash, rsa_private_key, rsa_n):
        pass
    def fonk6(self, signature, rsa_public_key, rsa_n, data_hash):
        pass
    def fonk7(self, public_key, private_key):
        pass
    def fonk8(self, x, y):
        pass
def fonk9():
    b2 = class1("b2")
    b3 = class1("b3")
    ma_rsa_private, ma_rsa_public, b4 = b2.fonk2()
    mo_rsa_private, mo_rsa_public, b5 = b3.fonk2()
    ma_d, b6 = b2.fonk3()
    mo_d, b7 = b3.fonk3()
    b8 = b2.fonk4(str(b6[0]), str(b6[1]))
    b9 = b2.fonk5(b8, ma_rsa_private, b4)
    b10 = b3.fonk4(str(b7[0]), str(b7[1]))
    b11 = b3.fonk5(b10, mo_rsa_private, b5)
    b12 = b2.fonk4(str(b7[0]), str(b7[1]))
    b13 = b2.fonk6(b11, mo_rsa_public, b5, b12)
    b14 = b3.fonk4(str(b6[0]), str(b6[1]))
    b15 = b3.fonk6(b9, ma_rsa_public, b4, b14)
    b16 = b2.fonk7(b7, ma_d)
    b17 = b3.fonk7(b6, mo_d)
    b18 = b2.fonk8(b16[0], b16[1])
    print("\n\nmatin verify rsa_sign:")
    print(b13)
    print("\nmohamad verify rsa_sign:")
    print(b15)
    print("\nmatin share key:")
    print(b16)
    print("\nmohamad share key:")
    print(b17)
    print("\ncheck point in curve ?")
    print(b18)
if b19 = = "__main__":
    fonk9()