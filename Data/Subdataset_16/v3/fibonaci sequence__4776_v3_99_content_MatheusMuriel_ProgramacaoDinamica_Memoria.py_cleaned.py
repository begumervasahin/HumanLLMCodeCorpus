class class1:
    def fonk1(self, b3, b4):
        self.b1 = {}
        self.b2 = {}
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b5, b6):
        b5 = str(b5)
        b6 = int(b6)
        if len(self.b1) >= self.b3:
            self.fonk4()
        self.b1[b5] = b6
        self.b2[b5] = 1
    def fonk3(self, b5):
        if b5 in self.b1:
            self.b2[b5] += 1
            return self.b1[b5]
        return -1
    def fonk4(self):
        print("Executing memory cleanup.")
        b7 = int(self.b3 * self.b4)
        while len(self.b1) > b7:
            b8 = min(self.b2.items(), key=lambda x: x[1])
            self.b1.pop(b8[0])
            self.b2.pop(b8[0])
if b9 = = "__main__":
    b10 = class1(b3=5, b4=0.7)
    b10.fonk2("1", 1)
    b10.fonk2("2", 1)
    b10.fonk2("3", 2)
    b10.fonk2("4", 3)
    b10.fonk2("5", 5)
    print(b10.fonk3("1"))
    b10.fonk2("6", 8)
    print(b10.fonk3("1"))
    print(b10.fonk3("6"))
