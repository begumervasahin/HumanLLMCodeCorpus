import os
import time
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = [[] for _ in range(b1)]
    def fonk2(self, key):
        a1 = 0.6180339887
        return int(self.b1 * ((hash(key) * a1) % 1))
    def fonk3(self, key):
        return hash(key) % self.b1
    def fonk4(self, b5, a2):
        return (b5 + a2) % self.b1
    def fonk5(self, b5, a2):
        return (b5 + a2**2) % self.b1
    def fonk6(self, key):
        if self.b3 = = 'multiplication':
            return self.fonk2(key)
        else:
            return self.fonk3(key)
    def fonk7(self, b5, a2):
        if self.b2 = = 'linear':
            return self.fonk4(b5, a2)
        else:
            return self.fonk5(b5, a2)
    def fonk8(self, key, value):
        b5 = self.fonk6(key)
        a2 = 0
        b6 = b5
        while self.b4[b6]:
            if self.b4[b6][0] == key:
                self.b4[b6].append(value)
                return
            a2 += 1
            b6 = self.fonk7(b5, a2)
        self.b4[b6] = [key, value]
    def fonk9(self, key):
        b5 = self.fonk6(key)
        a2 = 0
        b6 = b5
        while self.b4[b6]:
            if self.b4[b6][0] == key:
                return self.b4[b6][1:]
            a2 += 1
            b6 = self.fonk7(b5, a2)
        return None
    def fonk10(self):
        b7 = []
        for entry in self.b4:
            if entry:
                b7.append(entry[0])
        return b7
def fonk11(pasta):
    b8 = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    b9 = [arq for arq in b8 if os.path.isfile(arq)]
    return b9
def fonk12(arquivo, num, hashing):
    with open(arquivo, 'r') as arq:
        b10 = arq.read().lower()
    b10 = b10.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    b10 = b10.replace("\r", "").replace("\t", "").replace("\n", "")
    b10 = b10.split(" ")
    for b19 in b10:
        b11 = b10.b11(b19)
        b12 = True
        b13 = hashing.fonk9(b19)
        if b13:
            for value in b13:
                if value[0] == b11 and value[1] == num + 1:
                    b12 = False
            if b12:
                hashing.fonk8(b19, [b11, num + 1])
        else:
            hashing.fonk8(b19, [b11, num + 1])
b14 = {
    'ML': class1(1000000, 'linear', 'multiplication'),
    'MQ': class1(1000000, 'quadratic', 'multiplication'),
    'DL': class1(1000000, 'linear', 'division'),
    'DQ': class1(1000000, 'quadratic', 'division'),
}
def fonk13(method_key, method_desc):
    b15 = time.time()
    b9 = fonk11('base')
    for a2 in range(len(b9)):
        fonk12(b9[a2], a2, b14[method_key])
    for key in sorted(b14[method_key].fonk10()):
        b16 = b14[method_key].fonk9(key)
        print(key, b16[0][0], b9[(b16[0][1])-1])
    b17 = time.time()
    print(f'tempo para Hashing utilizando {method_desc}:', b17 - b15)
if b18 = = "__main__":
    fonk13('ML', 'metodo da multiplicacao e colizao linear')
    fonk13('MQ', 'metodo da multiplicacao e colizao Quadratica')
    fonk13('DL', 'metodo da Divisao e colizao linear')
    fonk13('DQ', 'metodo da Divisao e colizao Quadratica')
    while True:
        b19 = input("Digite uma b19:\n")
        if b19 in b14['ML'].fonk10():
            print(b14['ML'].fonk9(b19))
        else:
            print("Palavra nÃ£o encontrada.")