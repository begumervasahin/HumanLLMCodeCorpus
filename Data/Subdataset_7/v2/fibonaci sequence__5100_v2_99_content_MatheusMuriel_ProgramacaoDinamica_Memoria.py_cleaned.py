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
            self.fonk4(b5)
        self.b1[b5] = b6
        self.b2[b5] = 1
    def fonk3(self, b5):
        if b5 in self.b1:
            self.b2[b5] += 1
            return self.b1[b5]
        else:
            return -1
    def fonk4(self, current_iteration):
        print("Cleaning called at iteration", current_iteration)
        b7 = int(self.b3 * self.b4)
        for _ in range(b7):
            b8 = min(self.b2.items(), key=lambda x: x[1])
            self.b1.pop(b8[0])
            self.b2.pop(b8[0])
b9 = class1(b3=100, b4=0.5)
b9.fonk2("A", 10)
b9.fonk2("B", 20)
print(b9.fonk3("A"))
print(b9.fonk3("C"))