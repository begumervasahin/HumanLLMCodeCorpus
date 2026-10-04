class class1:
    def fonk1(self, b1):
        self.b1 = list(b1)
        self.b2 = list(range(len(b1)))
        self.b3 = [1] * len(b1)
    def fonk2(self, element):
        b4 = self.b1.b4(element)
        if self.b2[b4] != b4:
            self.b2[b4] = self.fonk2(self.b1[self.b2[b4]])
        return self.b2[b4]
    def fonk3(self, element_a, element_b):
        b5 = self.fonk2(element_a)
        b6 = self.fonk2(element_b)
        if b5 != b6:
            if self.b3[b5] > self.b3[b6]:
                self.b2[b6] = b5
            elif self.b3[b5] < self.b3[b6]:
                self.b2[b5] = b6
            else:
                self.b2[b6] = b5
                self.b3[b5] += 1
    def fonk4(self):
        return "\n".join(f"{element}: {self.fonk2(element)}" for element in self.b1)
if b7 = = "__main__":
    b1 = ['A', 'B', 'C', 'D', 'E']
    b8 = class1(b1)
    print("Initial sets:")
    print(b8)
    b8.fonk3('A', 'B')
    b8.fonk3('B', 'C')
    print("\nSets after some unions:")
    print(b8)
    b8.fonk3('D', 'E')
    b8.fonk3('C', 'D')
    print("\nFinal sets after all unions:")
    print(b8)