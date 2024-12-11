class class1:
    def fonk1(self):
        self.b1 = ""
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b2):
        if self.b1[b2] in 'aeiou':
            return False
        if self.b1[b2] == 'y':
            if b2 = = self.a2:
                return True
            else:
                return not self.fonk2(b2 - 1)
        return True
    def fonk3(self):
        a4 = 0
        b2 = self.a2
        while True:
            if b2 > self.a3:
                return a4
            if not self.fonk2(b2):
                break
            b2 += 1
        b2 += 1
        while True:
            while True:
                if b2 > self.a3:
                    return a4
                if self.fonk2(b2):
                    break
                b2 += 1
            b2 += 1
            a4 += 1
            while True:
                if b2 > self.a3:
                    return a4
                if not self.fonk2(b2):
                    break
                b2 += 1
            b2 += 1
    def fonk4(self):
        for b2 in range(self.a2, self.a3 + 1):
            if not self.fonk2(b2):
                return True
        return False
    def fonk5(self, j):
        if j < (self.a2 + 1):
            return False
        if self.b1[j] != self.b1[j - 1]:
            return False
        return self.fonk2(j)
    def fonk6(self, b2):
        if b2 < (self.a2 + 2) or not self.fonk2(b2) \
                or self.fonk2(b2 - 1) or not self.fonk2(b2 - 2):
            return False
        b3 = self.b1[b2]
        if b3 in 'wx':
            return False
        return True
    def fonk7(self, suffix):
        b4 = len(suffix)
        if suffix[b4 - 1] != self.b1[self.a3]:
            return False
        if b4 > (self.a3 - self.a2 + 1):
            return False
        if self.b1[self.a3 - b4 + 1:self.a3 + 1] != suffix:
            return False
        self.a1 = self.a3 - b4
        return True
    def fonk8(self, replacement):
        b4 = len(replacement)
        self.b1 = self.b1[:self.a3 + 1] + replacement + self.b1[self.a3 + b4 + 1:]
        self.a1 = self.a3 + b4
    def fonk9(self, suffix, replacement):
        if self.fonk7(suffix):
            self.fonk8(replacement)
    def fonk10(self):
        if self.b1[self.a1] == 's':
            if self.fonk7("sses"):
                self.a1 -= 2
            elif self.fonk7("ies"):
                self.fonk8("i")
            elif self.b1[self.a1 - 1] != 's':
                self.a1 -= 1
        if self.fonk7("eed"):
            if self.fonk3() > 0:
                self.a1 -= 1
        elif (self.fonk7("ed") or self.fonk7("ing")) and self.fonk4():
            self.a1 = self.a3
            if self.fonk7("at"):
                self.fonk8("ate")
            elif self.fonk7("bl"):
                self.fonk8("ble")
            elif self.fonk7("iz"):
                self.fonk8("ize")
            elif self.fonk5(self.a1):
                self.a1 -= 1
                b3 = self.b1[self.a1]
                if b3 in 'lsz':
                    self.a1 += 1
            elif (self.fonk3() == 1 and self.fonk6(self.a1)):
                self.fonk8("e")
    def fonk11(self):
        if (self.fonk7("y") and self.fonk4()):
            self.b1 = self.b1[:self.a1] + 'i' + self.b1[self.a1 + 1:]
    def fonk12(self):
        if self.b1[self.a1 - 1] == 'a':
            self.fonk9("ational", "ate")
            self.fonk9("tional", "tion")
        elif self.b1[self.a1 - 1] == 'c':
            self.fonk9("enci", "ence")
            self.fonk9("anci", "ance")
    def fonk13(self, b1):
        self.b1 = b1
        self.a1 = len(b1