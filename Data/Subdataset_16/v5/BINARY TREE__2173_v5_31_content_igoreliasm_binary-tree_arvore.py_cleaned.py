from b7 import No
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
    def fonk8(self, b5, valor):
        if self.b1:
            self.fonk9(b5, valor, self.b1)
        else:
            self.b1 = No(b5, valor)
        self.a1 += 1
    def fonk9(self, b5, valor, no_corrente):
        if b5 < no_corrente.b5:
            if no_corrente.tem_filho_esquerda():
                self.fonk9(b5, valor, no_corrente.b2)
            else:
                no_corrente.b2 = No(b5, valor, b8=no_corrente)
        else:
            if no_corrente.tem_filho_direita():
                self.fonk9(b5, valor, no_corrente.b3)
            else:
                no_corrente.b3 = No(b5, valor, b8=no_corrente)
    def fonk10(self, b5):
        if self.b1:
            b4 = self.fonk11(b5, self.b1)
            return b4.b10 if b4 else None
        return None
    def fonk11(self, b5, no_corrente):
        if no_corrente is None:
            return None
        if no_corrente.b5 = = b5:
            return no_corrente
        if b5 < no_corrente.b5:
            return self.fonk11(b5, no_corrente.b2)
        return self.fonk11(b5, no_corrente.b3)
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
    def fonk14(self, b7):
        if b7.tem_filho_direita():
            return self.fonk15(b7.b3)
        while b7.b8 and b7.eh_filho_direita():
            b7 = b7.b8
        return b7.b8
    def fonk15(self, b7):
        while b7.tem_filho_esquerda():
            b7 = b7.b2
        return b7
    def fonk16(self, b7):
        if b7.eh_folha():
            if b7.eh_filho_esquerda():
                b7.b8.b2 = None
            else:
                b7.b8.b3 = None
        elif b7.tem_filho_esquerda():
            if b7.eh_filho_esquerda():
                b7.b8.b2 = b7.b2
            else:
                b7.b8.b3 = b7.b2
            b7.b2.b8 = b7.b8
        else:
            if b7.eh_filho_esquerda():
                b7.b8.b2 = b7.b3
            else:
                b7.b8.b3 = b7.b3
            b7.b3.b8 = b7.b8
    def fonk17(self, no_corrente):
        if no_corrente.eh_folha():
            if no_corrente.eh_filho_esquerda():
                no_corrente.b8.b2 = None
            else:
                no_corrente.b8.b3 = None
        elif no_corrente.tem_todos_filhos():
            b9 = self.fonk14(no_corrente)
            self.fonk16(b9)
            no_corrente.b5 = b9.b5
            no_corrente.b10 = b9.b10
        else:
            b11 = no_corrente.b2 if no_corrente.tem_filho_esquerda() else no_corrente.b3
            if no_corrente.eh_filho_esquerda():
                no_corrente.b8.b2 = b11
            else:
                no_corrente.b8.b3 = b11
            b11.b8 = no_corrente.b8