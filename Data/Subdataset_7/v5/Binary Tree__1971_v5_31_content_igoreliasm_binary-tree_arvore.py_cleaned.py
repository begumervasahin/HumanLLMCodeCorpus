from no import No
class class1:
    def fonk1(b8):
        b8.b1 = None
        b8.a1 = 0
    def fonk2(b8, b5, valor):
        b8.fonk8(b5, valor)
    def fonk3(b8, b5):
        b8.fonk12(b5)
    def fonk4(b8):
        return b8.a1
    def fonk5(b8, b5):
        return b8.fonk10(b5)
    def fonk6(b8, b5):
        return bool(b8.fonk11(b5, b8.b1))
    def fonk7(b8):
        return b8.a1
    def fonk8(b8, b5, val):
        if b8.b1:
            b8.fonk9(b5, val, b8.b1)
        else:
            b8.b1 = No(b5, val)
        b8.a1 += 1
    def fonk9(b8, b5, val, b4):
        if b5 < b4.b5:
            if b4.temFilhoEsquerda():
                b8.fonk9(b5, val, b4.b2)
            else:
                b4.b2 = No(b5, val, b7=b4)
        else:
            if b4.temFilhoDireita():
                b8.fonk9(b5, val, b4.b3)
            else:
                b4.b3 = No(b5, val, b7=b4)
    def fonk10(b8, b5):
        b4 = b8.fonk11(b5, b8.b1)
        return b4.b11 if b4 else None
    def fonk11(b8, b5, b4):
        while b4:
            if b5 = = b4.b5:
                return b4
            elif b5 < b4.b5:
                b4 = b4.b2
            else:
                b4 = b4.b3
        return None
    def fonk12(b8, b5):
        b6 = b8.fonk11(b5, b8.b1)
        if not b6:
            raise KeyError('Chave não encontrada na árvore atual')
        b8.fonk16(b6)
        b8.a1 -= 1
    def fonk13(b8):
        b8.b1 = None
        b8.a1 = 0
        print("Sua árvore está vazia!")
    def fonk14(b8):
        if b8.temFilhoDireita():
            return b8.b3.fonk15()
        else:
            b7 = b8.b7
            while b7 and b8 = = b7.b3:
                b8 = b7
                b7 = b7.b7
            return b7
    def fonk15(b8):
        b9 = b8
        while b9.b2:
            b9 = b9.b2
        return b9
    def fonk16(b8, b4):
        if b4.ehFolha():
            if b4.b7:
                if b4 = = b4.b7.b2:
                    b4.b7.b2 = None
                else:
                    b4.b7.b3 = None
        elif b4.temTodosFilhos():
            b10 = b4.fonk14()
            b10.removerSucessor()
            b4.b5 = b10.b5
            b4.b11 = b10.b11
        else:
            b12 = b4.b2 if b4.temFilhoEsquerda() else b4.b3
            if b4.ehFilhoEsquerda():
                b4.b7.b2 = b12
            else:
                b4.b7.b3 = b12
            b12.b7 = b4.b7