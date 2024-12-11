class class1:
    def fonk1(self, b3, b4, b5):
        b1 = (b3 ** b4) % b5
        return b1
    def fonk2(self, b1, b6, b5):
        b2 = (b1 ** b6) % b5
        return b2
    def fonk3(self):
        b3 = input("Digite a b3: \t")
        while len(b3) > 128:
            print("Você ultrapassou o limite de caracteres.")
            b3 = input("Digite a b3 novamente: \t")
        print('=' * 5 + ' Digite as chaves públicas: ' + '=' * 5)
        b4 = int(input("Chave pública (e): \t"))
        b5 = int(input("Modulo (n): \t"))
        b1 = ''.join(chr(self.fonk1(ord(caractere), b4, b5)) for caractere in b3)
        print('Texto Criptografado: ', b1, '\n')
        return b1
    def fonk4(self, b1):
        print('=' * 5 + ' Digite as chaves privadas: ' + '=' * 5)
        b6 = int(input("Chave privada (d): \t"))
        b5 = int(input("Modulo (n): \t"))
        b2 = ''.join(chr(self.fonk2(ord(caractere), b6, b5)) for caractere in b1)
        print('Texto Simples: ', b2, '\n')
        return b2
b7 = class1()
b1 = b7.fonk3()
b7.fonk4(b1)