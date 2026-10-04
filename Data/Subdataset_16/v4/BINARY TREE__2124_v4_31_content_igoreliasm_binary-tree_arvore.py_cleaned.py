from no import No
class class1:
    def fonk1(self):
        self.b1 = None
        self.a1 = 0
    def fonk2(self, b5, valor):
        self.fonk8(b5, valor)
    def fonk3(self, b5):
        self.fonk12(b5)
    def fonk4(self):
        return self.a1
    def fonk5(self, b5):
        return self.fonk10(b5)
    def fonk6(self, b5):
        return self.fonk11(b5, self.b1) is not None
    def fonk7(self):
        return self.a1
    def fonk8(self, b5, val):
        if self.b1:
            self.fonk9(b5, val, self.b1)
        else:
            self.b1 = No(b5, val)
        self.a1 += 1
    def fonk9(self, b5, val, b10):
        if b5 < b10.b5:
            if b10.tem_filho_esquerda():
                self.fonk9(b5, val, b10.b2)
            else:
                b10.b2 = No(b5, val, b9=b10)
        else:
            if b10.tem_filho_direita():
                self.fonk9(b5, val, b10.b3)
            else:
                b10.b3 = No(b5, val, b9=b10)
    def fonk10(self, b5):
        if self.b1:
            b4 = self.fonk11(b5, self.b1)
            return b4.b11 if b4 else None
        return None
    def fonk11(self, b5, b10):
        if b10 is None:
            return None
        elif b10.b5 = = b5:
            return b10
        elif b5 < b10.b5:
            return self.fonk11(b5, b10.b2)
        else:
            return self.fonk11(b5, b10.b3)
    def fonk12(self, b5):
        if self.a1 > 1:
            b6 = self.fonk11(b5, self.b1)
            if b6:
                self.fonk17(b6)
                self.a1 -= 1
            else:
                raise KeyError('Chave não encontrada na árvore atual')
        elif self.a1 = = 1 and self.b1.b5 == b5:
            self.b1 = None
            self.a1 -= 1
        else:
            raise KeyError('Chave não encontrada na árvore atual')
    def fonk13(self):
        self.b1 = None
        self.a1 = 0
        print("Sua árvore está vazia!")
    def fonk14(self, no):
        b7 = None
        if no.tem_filho_direita():
            b7 = no.b3.fonk15()
        else:
            if no.b9:
                if no.eh_filho_esquerda():
                    b7 = no.b9
                else:
                    no.b9.b3 = None
                    b7 = no.b9.fonk14()
                    no.b9.b3 = no
        return b7
    def fonk15(self, no):
        b8 = no
        while b8.tem_filho_esquerda():
            b8 = b8.b2
        return b8
    def fonk16(self, no):
        if no.eh_folha():
            if no.eh_filho_esquerda():
                no.b9.b2 = None
            else:
                no.b9.b3 = None
        elif no.tem_algum_filho():
            if no.tem_filho_esquerda():
                if no.eh_filho_esquerda():
                    no.b9.b2 = no.b2
                else:
                    no.b9.b3 = no.b2
                    no.b2.b9 = no.b9
        else:
            if no.eh_filho_esquerda():
                no.b9.b2 = no.b3
            else:
                no.b9.b3 = no.b3
                no.b3.b9 = no.b9
    def fonk17(self, b10):
        if b10.eh_folha():
            if b10 = = b10.b9.b2:
                b10.b9.b2 = None
            else:
                b10.b9.b3 = None
        elif b10.tem_todos_filhos():
            b7 = self.fonk14(b10)
            self.fonk16(b7)
            b10.b5 = b7.b5
            b10.b11 = b7.b11
        else:
            if b10.tem_filho_esquerda():
                if b10.eh_filho_esquerda():
                    b10.b2.b9 = b10.b9
                    b10.b9.b2 = b10.b2
                else:
                    b10.b2.b9 = b10.b9
                    b10.b9.b3 = b10.b2
            else:
                if b10.eh_filho_esquerda():
                    b10.b3.b9 = b10.b9
                    b10.b9.b2 = b10.b3
                else:
                    b10.b3.b9 = b10.b9
                    b10.b9.b3 = b10.b3