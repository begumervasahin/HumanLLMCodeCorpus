from random import randint, choice
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class1(b1 = {self.b1}, b2={self.b2})'
    def fonk3(self, other):
        if isinstance(other, class1):
            return self.b2 = = other.b2
        return self.b2 = = other
    def fonk4(self, other):
        if isinstance(other, class1):
            return self.b2 > other.b2
        return self.b2 > other
    def fonk5(self, other):
        if isinstance(other, class1):
            return self.b2 < other.b2
        return self.b2 < other
    def fonk6(self, other):
        if isinstance(other, class1):
            return self.b2 >= other.b2
        return self.b2 >= other
    def fonk7(self, other):
        if isinstance(other, class1):
            return self.b2 <= other.b2
        return self.b2 <= other
    def fonk8(self, other):
        if isinstance(other, class1):
            return self.b2 != other.b2
        return self.b2 != other
class class2:
    def fonk9(self, num_cars):
        self.b3 = [class1(randint(1, 74), randint(1, 1000)) for _ in range(num_cars)]
    def fonk10(self):
        b4 = f'This is a b18 with {len(self.b3)} b3:'
        for b6 in self.b3:
            b4 += f'\n\t{b6}'
        return b4
    def fonk11(self, num, b5 = 'b2'):
        if b5 = = 'b2':
            b6 = class1(num, randint(1, 1000))
        else:
            b6 = class1(randint(1, 74), num)
        self.b3.append(b6)
        return b6
    def fonk12(self, b7 = True, b12='b2'):
        for i in range(len(self.b3) - 1, 0, -1):
            b8 = False
            for j in range(i):
                if (getattr(self.b3[j], b12) > getattr(self.b3[j + 1], b12)) == b7:
                    self.b3[j], self.b3[j + 1] = self.b3[j + 1], self.b3[j]
                    b8 = True
            if not b8:
                break
    def fonk13(self, b7 = True, b12='b2'):
        for i in range(1, len(self.b3)):
            b9 = self.b3[i]
            b10 = i - 1
            while b10 >= 0 and (getattr(b9, b12) < getattr(self.b3[b10], b12)) == b7:
                self.b3[b10 + 1] = self.b3[b10]
                b10 -= 1
            self.b3[b10 + 1] = b9
    def fonk14(self, b7 = True, b12='b2'):
        for i in range(len(self.b3)):
            b11 = i
            for j in range(i + 1, len(self.b3)):
                if (getattr(self.b3[j], b12) < getattr(self.b3[b11], b12)) == b7:
                    b11 = j
            if b11 != i:
                self.b3[i], self.b3[b11] = self.b3[b11], self.b3[i]
    def fonk15(self, value, b12 = 'b2', b7=True):
        b16, b13 = 0, len(self.b3) - 1
        while b16 <= b13:
            b14 = (b16 + b13)
            b15 = getattr(self.b3[b14], b12)
            if b15 = = value:
                return self.b3[b14]
            elif (b15 < value) == b7:
                b16 = b14 + 1
            else:
                b13 = b14 - 1
        return None
    def fonk16(self, value, b12 = 'b2', b7=True):
        b17 = choice([self.selection_sort, self.insertion_sort, self.bubble_sort])
        b17(b7, b12)
        return self.fonk15(value, b12, b7)
    def fonk17(self, b1):
        self.fonk13(b12 = 'b1')
        return self.fonk15(b1, b12 = 'b1')
    def fonk18(self, b6):
        self.b3.remove(b6)
        return b6
class class3:
    b18 = None
    @classmethod
    def fonk19(cls, num_cars):
        cls.b18 = class2(num_cars)
    @classmethod
    def fonk20(cls):
        cls.b18 = None
if b19 = = "__main__":
    class3.fonk19(10)
    print(class3.b18)
    print("\nAdding a b6 with 50 b2:")
    class3.b18.fonk11(50)
    print(class3.b18)
    print("\nFinding a b6 with 50 b2:")
    b20 = class3.b18.fonk16(50, 'b2')
    print(b20)
    print("\nSorting b3 by b2 in b7 order:")
    class3.b18.fonk12()
    print(class3.b18)
    print("\nDestroying the found b6:")
    class3.b18.fonk18(b20)
    print(class3.b18)