class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return f"class1 object can be used to sort a list:\a2{self.b1}"
    def fonk3(self, b2 = False):
        a1 = 0
        a2 = 1
        while a2 < len(self.b1):
            for i in range(len(self.b1) - a2):
                if (b2 and self.b1[i] < self.b1[i + 1]) or (not b2 and self.b1[i] > self.b1[i + 1]):
                    self.b1[i], self.b1[i + 1] = self.b1[i + 1], self.b1[i]
                    a1 += 1
            if a1 = = 0:
                break
            else:
                a2 += 1
        return self.b1
    def fonk4(self, b2 = False):
        for i in range(1, len(self.b1)):
            b3 = self.b1[i]
            b4 = i - 1
            while b4 >= 0 and ((b2 and self.b1[b4] < b3) or (not b2 and self.b1[b4] > b3)):
                self.b1[b4 + 1] = self.b1[b4]
                b4 -= 1
            self.b1[b4 + 1] = b3
        return self.b1
def fonk5(lst, target):
    a3 = 0
    b5 = len(lst) - 1
    while a3 <= b5:
        b6 = (a3 + b5)
        if lst[b6] == target:
            return b6
        elif lst[b6] < target:
            a3 = b6 + 1
        else:
            b5 = b6 - 1
    return a3
def fonk6(a2, lst):
    if not lst:
        lst.append(a2)
    else:
        b7 = fonk5(lst, a2)
        lst.insert(b7, a2)
    return lst