class class1:
    pass
class class2(class1):
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = self.b1 * self.b2
        b4 = (self.b1 - 1) * (self.b2 - 1)
        print("Escolha sua chave pública:")
        print(self.fonk5(b4))
        b5 = int(input("Escolha o valor de b5: "))
        b6 = self.fonk6(b5, b4)
        print("\nChaves públicas (b5 = {}, b3={})".format(b5, b3))
        print("class2 privadas (b6 = {}, b3={})".format(b6, b3))
    def fonk3(self, a, b7):
        while a != 0:
            a, b7 = b7 % a, a
        return b7
    def fonk4(self, a, b8):
        for x in range(1, b8):
            if (a * x) % b8 = = 1:
                return x
        print('Não há inverso modular para o bloco.')
        return None
    def fonk5(self, b4):
        b9 = []
        for x in range(2, b4):
            if self.fonk3(b4, x) == 1 and self.fonk4(x, b4) is not None:
                b9.append(x)
        return b9
    def fonk6(self, b5, b4):
        return self.fonk4(b5, b4)
a1 = 17
a2 = 19
b10 = class2(a1, a2)
b10.fonk2()