class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return f"class1 instance with the list: {self.b1}"
    def fonk3(self):
        b2 = len(self.b1)
        for i in range(b2):
            b3 = False
            for j in range(b2 - i - 1):
                if self.b1[j] > self.b1[j + 1]:
                    self.b1[j], self.b1[j + 1] = self.b1[j + 1], self.b1[j]
                    b3 = True
            if not b3:
                break
        return self.b1
    def fonk4(self):
        b2 = len(self.b1)
        for i in range(b2):
            b3 = False
            for j in range(b2 - i - 1):
                if self.b1[j] < self.b1[j + 1]:
                    self.b1[j], self.b1[j + 1] = self.b1[j + 1], self.b1[j]
                    b3 = True
            if not b3:
                break
        return self.b1
def fonk5(lst, b2):
    b6, b4 = 0, len(lst) - 1
    while b6 <= b4:
        b5 = (b6 + b4)
        if lst[b5] < b2:
            b6 = b5 + 1
        elif lst[b5] > b2:
            b4 = b5 - 1
        else:
            return b5
    return b6
def fonk6(b2, lst):
    if not lst:
        lst.append(b2)
    else:
        b7 = fonk5(lst, b2)
        lst.insert(b7, b2)
    return lst
if b8 = = "__main__":
    b1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    b9 = class1(b1)
    print("Original list:", b1)
    print("Sorted list (ascending):", b9.fonk3())
    print("Sorted list (descending):", b9.fonk4())
    b10 = [1, 3, 5, 7, 9]
    a1 = 6
    print(f"Inserting {a1} into {b10}:")
    b11 = fonk6(a1, b10)
    print("Updated list:", b11)