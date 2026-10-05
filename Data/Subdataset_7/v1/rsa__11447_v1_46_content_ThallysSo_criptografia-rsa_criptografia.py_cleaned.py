class class1(object):
    def fonk1(self, b2, b4, b5):
        b1 = (b2**b4) % b5
        return b1
    def fonk2(self, b1, b7, b5):
        b2 = (b1**b7) % b5
        return b2
    def fonk3(self):
        b3 = input("Digite a mensagem: \t")
        while len(b3) > 128:
            print("Você ultrapassou o limite de caracteres.")
            b3 = input("Digite a mensagem novamente: \t")
        print('='*5 + ' Digite as chaves públicas: ' + '='*5)
        b4 = int(input("Chave b4: \t"))
        b5 = int(input("Chave b5: \t"))
        b6 = ''.join(chr(self.fonk1(ord(x), b4, b5)) for x in b3)
        print('Texto Criptografado: ', b6, '\b5')
        return b6
    def fonk4(self, b3):
        print('='*5 + ' Digite as chaves privadas: ' + '='*5)
        b7 = int(input("Chave b7: \t"))
        b5 = int(input("Chave b5: \t"))
        b8 = ''.join(chr(self.fonk2(ord(x), b7, b5)) for x in b3)
        return print('Texto Simples: ', b8, '\b5')
b9 = class1()
b10 = b9.fonk3()
b9.fonk4(b10)