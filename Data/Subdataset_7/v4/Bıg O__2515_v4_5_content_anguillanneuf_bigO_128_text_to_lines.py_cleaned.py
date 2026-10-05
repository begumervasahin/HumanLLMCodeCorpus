from itertools import product, combinations
class class1:
    def fonk1(self, b1 = "", b2=80):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        for b5 in range(len(self.b1)):
            if not self.b1[b5].isspace():
                if b5 = = 0 or self.b1[b5 - 1].isspace():
                    self.b3.append(b5)
                if self.b3 and b5 - self.b3[-1] > self.b2:
                    print(f"\"{self.b1[self.b3[-1]:b5 + 1]}\" is longer than the allowed line b2 {self.b2}.")
                    print("Please consider adjusting the line b2.")
                    self.b3 = []
        self.b3.append(len(self.b1))
    def fonk3(self, b7, b6 = False):
        if not b6:
            if b7 = = len(self.b3) - 1:
                return None
            b8 = b7
            b9 = len(self.b3) - 1
            if self.b3[b9] - self.b3[b8] <= self.b2:
                return b9
            a1 = 1
        else:
            if b7 = = 0:
                return None
            b8 = 0
            b9 = b7
            if self.b3[b9] - self.b3[b8] <= self.b2:
                return b8
            a1 = -1
        while b8 < b9:
            b10 = (b8 + b9)
            if self.b3[b10 - 1] <= self.b3[b7] + a1 * self.b2 <= self.b3[b10]:
                b7 = b10 - 1 * (not b6)
                break
            elif self.b3[b10] > self.b3[b7] + a1 * self.b2:
                b9 = b10
            else:
                b8 = b10
        return b7
    def fonk4(self):
        b11 = []
        b7 = 0
        while b7 is not None and b7 <= len(self.b3):
            b11.append((b7, self.b3[b7]))
            b7 = self.fonk3(b7)
        b12 = []
        b7 = len(self.b3) - 1
        while b7 is not None and b7 >= 0:
            b12.append((b7, self.b3[b7]))
            b7 = self.fonk3(b7, b6=True)
        b13 = float('inf')
        b14 = []
        for back, front in zip(b12[::-1], b11):
            b14.append(range(back[0], front[0] + 1))
        a2 = 0
        for b18 in product(*b14):
            a2 += 1
            a3 = 0
            b15 = True
            for index in range(1, len(b18)):
                b16 = self.b3[b18[index]] - self.b3[b18[index - 1]]
                if b16 > self.b2:
                    a3 = float('inf')
                    b15 = False
                    break
                else:
                    a3 += (self.b2 - b16) ** 2
            if b15:
                self.b4 = [self.b3[index] for index in b18]
        print(f"My solution runs {a2} times.")
        print(f"{self.b4} has least a3 of {b13}")
    def fonk5(self):
        b3 = self.b3[1:len(self.b3) - 1]
        b17 = len(self.b1)
        b13 = float('inf')
        a2 = 0
        for b18 in combinations(b3, b17):
            b15 = True
            a3 = 0
            b18 = [0] + list(b18) + [len(self.b1)]
            a2 += 1
            for index in range(1, len(b18)):
                b16 = b18[index] - b18[index - 1]
                if b16 > self.b2:
                    a3 = float('inf')
                    b15 = False
                    break
                else:
                    a3 += (self.b2 - b16) ** 2
            if a3 < b13:
                b13 = a3
                self.b4 = b18
        print(f"Brute force solution runs {a2} times.")
        print(f"{self.b4} has least a3 of {b13}")
    def fonk6(self):
        b19 = ['']
        b7 = 0
        a4 = 0
        for border in self.b4:
            if border - a4 < self.b2:
                b19[-1] += self.b1[b7:border]
            else:
                b19.append(self.b1[b7:border])
                a4 = b7
            b7 = border
        return b19
if b20 = = "__main__":
    b1 = "Try this: Given a string of English text and a paragraph b2, design an algorithm to break the " \
               "texts into b19 not exceeding the paragraph b2, and not too jagged."
    b19 = Lines(b1, 80)
    b19.fonk2()
    b19.fonk5()
    b19.fonk4()
    print(b19.fonk6())