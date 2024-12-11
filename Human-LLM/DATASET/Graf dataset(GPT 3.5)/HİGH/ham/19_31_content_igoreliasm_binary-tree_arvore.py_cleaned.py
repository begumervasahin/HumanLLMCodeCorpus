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
        if self.fonk11(b5, self.b1):
            return True
        else:
            return False
    def fonk7(self):
        return self.a1
    def fonk8(self, b5, val):
        if self.b1:
            self.fonk9(b5, val, self.b1)
        else:
            self.b1 = No(b5, val)
        self.a1 = self.a1 + 1
    def fonk9(self, b5, val, b11):
        if b5 < b11.b5:
            if b11.temFilhoEsquerda():
                self.fonk9(b5, val, b11.b2)
            else:
                b11.b2 = No(b5, val, b10 = b11)
        else:
            if b11.temFilhoDireita():
                self.fonk9(b5, val, b11.b3)
            else:
                b11.b3 = No(b5, val, b10 = b11)
    def fonk10(self, b5):
        if self.b1:
            b4 = self.fonk11(b5, self.b1)
            if b4:
                return b4.b12
            else:
               return None
        else:
            return None
    def fonk11(self, b5, b11):
        if not b11:
            return None
        elif b11.b5 = = b5:
           return b11
        elif b5 < b11.b5:
            return self.fonk11(b5, b11.temFilhoEsquerda)
        else:
            return self.fonk11(b5, b11.temFilhoDireita)
    def fonk12(self, b5):
        if self.a1 > 1:
            b6 = self.fonk11(b5, self.b1)
            if b6:
                self.fonk17(b6)
                self.a1 = self.a1 - 1
            else:
                raise KeyError('Chave nao encontrada na b7 atual')
        elif self.a1 = = 1 and self.b1.b5 == b5:
            self.b1 = None
            self.a1 = self.a1 - 1
        else:
            raise KeyError('Chave nao encontrada na b7 atual')
    def fonk13(self,b7):
        if b7!=None:
            b7 = None
            self.a1 = 0
            print("Sua class1 esta vazia!")
        else:
            print("Sua class1 esta vazia!")
    def fonk14(self):
        b8 = None
        if self.temFilhoDireita():
            b8 = self.b3.fonk15()
        else:
            if self.b10:
                if self.ehFilhoEsquerda():
                    b8 = self.b10
                else:
                    self.b10.b3 = None
                    b8 = self.b10.fonk14()
                    self.b10.b3 = self
        return b8
    def fonk15(self):
        b9 = self
        while b9.temFilhoEsquerda():
            b9 = b9.b2
        return current
    def fonk16(self):
        if self.ehFolha():
            if self.ehFilhoEsquerda():
                self.b10.b2 = None
            else:
                self.b10.b3 = None
        elif self.temAlgumFilho():
            if self.temFilhoEsquerda():
                if self.ehFilhoEsquerda():
                    self.b10.b2 = self.b2
                else:
                    self.b10.b3 = self.b2
                    self.b2.b10 = self.b10
        else:
            if self.ehFilhoEsquerda():
                self.b10.b2 = self.b3
            else:
                self.b10.b3 = self.b3
                self.b3.b10 = self.b10
    def fonk17(self, b11):
        if b11.ehFolha():
            if b11 = = b11.b10.b2:
                b11.b10.b2 = None
            else:
                b11.b10.b3 = None
        elif b11.temTodosFilhos():
            b8 = b11.b8()
            b8.fonk16()
            b11.b5 = b8.b5
            b11.b12 = b8.b12
        else:
            if b11.temFilhoEsquerda():
                if b11.ehFilhoEsquerda():
                    b11.b2.b10 = b11.b10
                    b11.b10.b2 = b11.b2
                elif b11.ehFilhoEsquerda():
                    b11.b2.b10 = b11.b10
                    b11.b10.b3 = b11.b2
                else:
                    b11.alterarDadosNo(
                        b11.b2.b5,
                        b11.b2.b12,
                        b11.b2.b2,
                        b11.b2.b3
                )
            else:
                if b11.ehFilhoEsquerda():
                    b11.b3.b10 = b11.b10
                    b11.b10.b2 = b11.b3
                elif b11.ehFilhoDireita():
                    b11.b3.b10 = b11.b10
                    b11.b10.b3 = b11.b3
                else:
                    b11.alterarDadosNo(
                        b11.b3.b5,
                        b11.b3.b12,
                        b11.b3.b2,
                        b11.b3.b3
                    )