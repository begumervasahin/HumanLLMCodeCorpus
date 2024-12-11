import Dictionary as dict
class class1:
    def fonk1(self):
        self.b1 = dict.my_dictionary()
    def fonk2(self, data):
        a1 = -1
        for b3 in data:
            b2 = self.fonk3(b3)
            a1 += 1
            b3 = f"{b3},{a1}"
            if b2 in self.b1:
                self.b1.update(b2, b3)
            else:
                self.b1.add(b2, b3)
        return self.b1
    def fonk3(self, name):
        b2 = ''.join(w[0] for w in name.split())
        return ''.join(sorted(b2))
    def fonk4(self, b2):
        b4 = 1 << len(b2)
        b5 = len(b2)
        b6 = set()
        for i in range(1, b4-1):
            b7 = bin(i)[2:].zfill(b5)
            b8 = ''
            for j in range(b5):
                if b7[j] == '1' and not b2[j].isdigit():
                    b8 += b2[j]
            b6.add(b8)
        return list(b6)