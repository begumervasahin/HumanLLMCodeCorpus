class class1:
    def fonk1(self, b6, b3, b4):
        b1 = (b6 ** b3) % b4
        return b1
    def fonk2(self, b1, b5, b4):
        b2 = (b1 ** b5) % b4
        return b2
    def fonk3(self):
        print('=' * 5 + ' Digite as chaves públicas: ' + '=' * 5)
        b3 = int(input("Chave pública (e): \t"))
        b4 = int(input("Módulo (n): \t"))
        return b3, b4
    def fonk4(self):
        print('=' * 5 + ' Digite as chaves privadas: ' + '=' * 5)
        b5 = int(input("Chave privada (d): \t"))
        b4 = int(input("Módulo (n): \t"))
        return b5, b4
    def fonk5(self):
        b6 = input("Digite a b6: \t")
        while len(b6) > 128:
            print("Você ultrapassou o limite de caracteres.")
            b6 = input("Digite a b6 novamente: \t")
        b3, b4 = self.fonk3()
        b1 = ''.join(chr(self.fonk1(ord(caractere), b3, b4)) for caractere in b6)
        print('Texto Criptografado: ', b1, '\n')
        return b1
    def fonk6(self, b1):
        b5, b4 = self.fonk4()
        b2 = ''.join(chr(self.fonk2(ord(caractere), b5, b4)) for caractere in b1)
        print('Texto Simples: ', b2, '\n')
        return b2
b7 = class1()
b1 = b7.fonk5()
b7.fonk6(b1)