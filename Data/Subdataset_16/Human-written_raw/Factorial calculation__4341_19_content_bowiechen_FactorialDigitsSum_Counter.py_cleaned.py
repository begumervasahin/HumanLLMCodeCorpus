class class1:
    b1 = []
    a1 = 0
    b2 = False
    def fonk1(self, a1, b3 = 0, zeros=True):
        self.a1 = a1
        if b3 != 0:
            self.b1 = list(str(b3))
            for counter, value in enumerate(self.b1):
                self.b1[counter] = int(value)
            self.b1.reverse()
            while len(self.b1) < a1:
                self.b1.append(0)
            self.b1.reverse()
        else:
            for b4 in range(a1):
                if zeros:
                    self.b1.append(0)
                else:
                    self.b1.append(1)
    def fonk2(self):
        self.b1[len(self.b1)-1] += 1
        for b4 in range(self.a1-1, -1, -1):
            if self.b1[b4] > 9:
                if b4 = = 0:
                    self.b2 = True
                self.b1[b4] = 0
                if b4-1 >= 0:
                    self.b1[b4-1] += 1
    def fonk3(self):
        b5 = ''
        for b4 in self.b1:
            b5 += str(b4)
        return int(b5)
    def fonk4(self):
        return self.b1