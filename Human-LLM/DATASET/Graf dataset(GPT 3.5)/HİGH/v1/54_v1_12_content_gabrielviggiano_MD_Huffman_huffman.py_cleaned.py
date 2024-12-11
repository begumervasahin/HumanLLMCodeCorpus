import os
from collections import Counter
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return repr((self.b1, self.b2, self.b3))
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b15):
        self.b6 = b15
    def fonk5(self, b8):
        self.b7 = [b8]
        return
    def fonk6(self, b8):
        for i in self.b7:
            if i.b1 = = b8.b1:
                i.b2 += 1
                self.b7 = sorted(self.b7, key=lambda no: no.b2)
                return
        self.b7 += [b8]
        self.b7 = sorted(self.b7, key=lambda no: no.b2)
    def fonk7(self):
        for l in self.b6:
            if self.b7 = = 0:
                self.fonk5(class1(l, 1, '', None, None))
            else:
                self.fonk6(class1(l, 1, '', None, None))
        return
    def fonk8(self):
        for elem in self.b7:
            print(elem)
        return
    def fonk9(self):
        self.fonk7()
        while len(self.b7) > 1:
            b8 = class1("", self.b7[0].b2 + self.b7[1].b2, '', self.b7[0], self.b7[1])
            del self.b7[0]
            del self.b7[0]
            self.b7 += [b8]
            self.b7 = sorted(self.b7, key=lambda no: no.b2)
        return
class class3:
    def fonk10(self, no):
        if no is None:
            return
        if no.b4 is not None:
            no.b4.b3 = no.b3 + '1'
            self.fonk10(no.b4)
        if no.b5 is not None:
            no.b5.b3 = no.b3 + '0'
            self.fonk10(no.b5)
        return
    def fonk11(self, b10, l):
        b3 = ''
        if b10.b1 = = l:
            b3 = b10.b3
        if b10.b4 is not None:
            b3 = self.fonk11(b10.b4, l)
        if b3 = = '':
            if b10.b5 is not None:
                b3 = self.fonk11(b10.b5, l)
        return b3
    def fonk12(self, b10, b6):
        b9 = ''
        for l in b6:
            b9 += self.fonk11(b10, l)
        return b9
    def fonk13(self, arvore2, textoBinario):
        b10 = arvore2
        b9 = ''
        for b3 in textoBinario:
            if b3 = = '1':
                if b10.b4 is not None:
                    b10 = b10.b4
                    if b10.b4 is None and b10.b5 is None:
                        b9 += (b10.b1)
                        b10 = arvore2
            else:
                if b10.b5 is not None:
                    b10 = b10.b5
                    if b10.b4 is None and b10.b5 is None:
                        b9 += (b10.b1)
                        b10 = arvore2
        return b9
    def fonk14(self, no):
        if no is None:
            return
        if no.b4 is not None:
            self.fonk14(no.b4)
        if no.fonk3():
            print(no)
        if no.b5 is not None:
            self.fonk14(no.b5)
        return
def fonk15(b15):
    b11 = Counter(b15)
    return b11
def fonk16(b13):
    if not os.path.isfile(b13):
        print("Arquivo não encontrado!")
        exit()
    else:
        with open(b13, "r") as arquivo:
            b6 = arquivo.read()
        return b6
def fonk17(b13, b6):
    try:
        b12 = open(b13, 'w')
        b12.write(b6)
        b12.close()
    except IOError:
        raise print("Erro ao criar o arquivo!")
def fonk18(args):
    print("PARA INICIAR O PROGRAMA, INSIRA O NOME DO ARQUIVO EM QUE A PALAVRA A SER COMPRIMIDA SE ENCONTRA")
    b13 = input("Nome: ")
    b14 = fonk16(b13)
    b15 = list(fonk16(b13))
    b16 = class3()
    b17 = class2(b15)
    b17.fonk9()
    b16.fonk10(b17.b7[0])
    print("--------------------- EXECUÇÃO DO CODIGO DE HUFFMAN ---------------------")
    print("Palavra inserida:", b14)
    print("")
    print("Frequencia dos caracteres:")
    b18 = fonk15(b15)
    print(b18)
    print("")
    print("Arvore criada com sucesso!")
    print("")
    print("Tabela de b16:")
    b16.fonk14(b17.b7[0])
    print("")
    b19 = b16.fonk12(b17.b7[0], b17.b6)
    print("Palavra comprimida para binário:", b19)
    print("")
    b20 = b16.fonk13(b17.b7[0], b16.fonk12(b17.b7[0], b17.b6))
    print("Palavra descomprimida:", b20)
    print("")
    fonk17("b9.txt", ("Palavra Inserida:" + b14 + "\n" +
                                 "Palavra Comprimida: " + b19 + "\n" +
                                 "Palavra Descomprimida: " + b20 + "\n"
    ))
    print("Arquivo de saida gerado com sucesso!")
    return 0
if b21 = = '__main__':
    import sys
    sys.exit(fonk18(sys.argv))