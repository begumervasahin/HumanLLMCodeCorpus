class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None, b5=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return self.b1 is not None
    def fonk3(self):
        return self.b4 is not None
    def fonk4(self):
        return not (self.b1 or self.b4)
    def fonk5(self):
        return self.b1 or self.b4
    def fonk6(self):
        return self.b1 and self.b4
    def fonk7(self):
        return self.b5 and self.b5.b1 = = self
    def fonk8(self):
        return self.b5 and self.b5.b4 = = self
    def fonk9(self, b2, b3, b1, b4):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
        if self.fonk2():
            self.b1.b5 = self
        if self.fonk3():
            self.b4.b5 = self
class class2:
    def fonk10(self):
        self.b6 = None
        self.a1 = 0
    def fonk11(self, b2, valor):
        self.fonk17(b2, valor)
    def fonk12(self, b2):
        self.fonk21(b2)
    def fonk13(self):
        return self.a1
    def fonk14(self, b2):
        return self.fonk19(b2)
    def fonk15(self, b2):
        return self.fonk20(b2, self.b6) is not None
    def fonk16(self):
        return self.a1
    def fonk17(self, b2, valor):
        if self.b6:
            self.fonk18(b2, valor, self.b6)
        else:
            self.b6 = class1(b2, valor)
        self.a1 += 1
    def fonk18(self, b2, valor, b11):
        if b2 < b11.b2:
            if b11.fonk2():
                self.fonk18(b2, valor, b11.b1)
            else:
                b11.b1 = class1(b2, valor, b5=b11)
        else:
            if b11.fonk3():
                self.fonk18(b2, valor, b11.b4)
            else:
                b11.b4 = class1(b2, valor, b5=b11)
    def fonk19(self, b2):
        if self.b6:
            b7 = self.fonk20(b2, self.b6)
            return b7.b3 if b7 else None
        return None
    def fonk20(self, b2, b11):
        if not b11:
            return None
        elif b11.b2 = = b2:
            return b11
        elif b2 < b11.b2:
            return self.fonk20(b2, b11.b1)
        else:
            return self.fonk20(b2, b11.b4)
    def fonk21(self, b2):
        if self.a1 > 1:
            b8 = self.fonk20(b2, self.b6)
            if b8:
                self.fonk26(b8)
                self.a1 -= 1
            else:
                raise KeyError('Chave não encontrada na árvore atual')
        elif self.a1 = = 1 and self.b6.b2 == b2:
            self.b6 = None
            self.a1 -= 1
        else:
            raise KeyError('Chave não encontrada na árvore atual')
    def fonk22(self):
        self.b6 = None
        self.a1 = 0
        print("Sua Árvore está vazia!")
    def fonk23(self, node):
        b9 = None
        if node.fonk3():
            b9 = self.fonk24(node.b4)
        else:
            if node.b5:
                if node.fonk7():
                    b9 = node.b5
                else:
                    node.b5.b4 = None
                    b9 = self.fonk23(node.b5)
                    node.b5.b4 = node
        return b9
    def fonk24(self, node):
        b10 = node
        while b10.fonk2():
            b10 = b10.b1
        return b10
    def fonk25(self, b11):
        if b11.fonk4():
            if b11.fonk7():
                b11.b5.b1 = None
            else:
                b11.b5.b4 = None
        elif b11.fonk5():
            if b11.fonk2():
                if b11.fonk7():
                    b11.b5.b1 = b11.b1
                else:
                    b11.b5.b4 = b11.b1
                b11.b1.b5 = b11.b5
            else:
                if b11.fonk7():
                    b11.b5.b1 = b11.b4
                else:
                    b11.b5.b4 = b11.b4
                b11.b4.b5 = b11.b5
    def fonk26(self, b11):
        if b11.fonk4():
            if b11 = = b11.b5.b1:
                b11.b5.b1 = None
            else:
                b11.b5.b4 = None
        elif b11.fonk6():
            b9 = self.fonk23(b11)
            self.fonk25(b9)
            b11.b2 = b9.b2
            b11.b3 = b9.b3
        else:
            if b11.fonk2():
                if b11.fonk7():
                    b11.b1.b5 = b11.b5
                    b11.b5.b1 = b11.b1
                elif b11.fonk8():
                    b11.b1.b5 = b11.b5
                    b11.b5.b4 = b11.b1
                else:
                    b11.fonk9(
                        b11.b1.b2,
                        b11.b1.b3,
                        b11.b1.b1,
                        b11.b1.b4
                    )
            else:
                if b11.fonk7():
                    b11.b4.b5 = b11.b5
                    b11.b5.b1 = b11.b4
                elif b11.fonk8():
                    b11.b4.b5 = b11.b5
                    b11.b5.b4 = b11.b4
                else:
                    b11.fonk9(
                        b11.b4.b2,
                        b11.b4.b3,
                        b11.b4.b1,
                        b11.b4.b4
                    )
if b12 = = '__main__':
    b13 = class2()
    b13.fonk17(10, 'Valor 10')
    b13.fonk17(5, 'Valor 5')
    b13.fonk17(15, 'Valor 15')
    print("Árvore contém b2 10:", 10 in b13)
    print("Valor associado à b2 10:", b13[10])
    b13.fonk21(10)
    print("Árvore após deletar b2 10:")
    print("Árvore contém b2 10:", 10 in b13)
    b13.fonk22()
    print("Árvore após esvaziar:")
    print("Árvore contém b2 5:", 5 in b13)