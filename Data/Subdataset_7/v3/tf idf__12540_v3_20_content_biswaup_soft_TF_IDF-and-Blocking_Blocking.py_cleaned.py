class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b3, value):
        self.b1[b3] = value
    def fonk3(self, b3, value):
        self.b1[b3] = value
    def fonk4(self):
        return self.b1
class class2:
    def fonk5(self, b11):
        b2 = class1()
        a1 = -1
        for index, item in enumerate(b11):
            b3 = self.fonk6(item)
            a1 += 1
            b4 = f"{item},{a1}"
            if b3 in b2.fonk4():
                b2.fonk3(b3, b4)
            else:
                b2.fonk2(b3, b4)
        return b2
    def fonk6(self, name):
        b3 = ''.join(sorted(w[0] for w in name.split()))
        return b3
    def fonk7(self, b3):
        b5 = 1 << len(b3)
        b6 = len(b3)
        b7 = []
        for i in range(1, b5 - 1):
            b8 = bin(i)[2:].zfill(b6)
            b9 = ''.join(b3[j] for j in range(b6) if b8[j] == '1' and not b3[j].isdigit())
            b7.append(b9)
        return list(set(b7))
if b10 = = "__main__":
    b11 = ["John Doe", "Jane Smith", "Alice Johnson"]
    b12 = class2()
    b2 = b12.fonk5(b11)
    print("Hash Table:")
    print(b2.fonk4())
    b3 = "JhonsDoe"
    b13 = b12.fonk7(b3)
    print("\nKeys for '{}' after b12:".format(b3))
    print(b13)
