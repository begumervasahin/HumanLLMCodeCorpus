
import Dictionary as dict
class class1:
    def fonk1(self, data):
        b1 = dict.my_dictionary()
        a1 = -1
        for b3 in data:
            b2 = self.fonk2(b3)
            a1 = a1 + 1
            b3 = b3 + ',' + str(a1)
            if b2 in b1:
                b1.update(b2, b3)
            else:
                b1.add(b2, b3)
        return b1
    def fonk2(self, name):
        b2 = ''
        for w in name.split():
            b2 = b2 + w[0]
        b2 = ''.join(sorted(b2))
        return b2
    def fonk3(self, b2):
        b4 = 1 << len(b2)
        b5 = len(b2)
        b6 = []
        for i in range(1, b4-1, 1):
            b7 = bin(i)[2:].zfill(b5)
            b8 = ''
            for j in range(0, len(b7)):
                if j < b5:
                    if b7[j] == '1' and not b2[j].isdigit():
                        b8 = b8 + b2[j]
            b6.append(b8)
        return list(set(b6))