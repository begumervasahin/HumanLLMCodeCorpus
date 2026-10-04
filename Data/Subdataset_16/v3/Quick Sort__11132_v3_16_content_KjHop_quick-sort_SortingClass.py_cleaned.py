class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, number):
        self.b1.append(number)
    def fonk3(self):
        return self.b1
    def fonk4(self):
        for number in self.b1:
            print(number)
    def fonk5(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            b2 = arr[-1]
            b3 = [num for num in arr if num < b2]
            b4 = [num for num in arr if num == b2]
            b5 = [num for num in arr if num > b2]
            return self.fonk5(b3) + b4 + self.fonk5(b5)
if b6 = = "__main__":
    b7 = class1()
    b8 = [34, 7, 23, 32, 5, 62, 32, 7]
    for number in b8:
        b7.fonk2(number)
    print("Original list:")
    b7.fonk4()
    b9 = b7.fonk5(b7.fonk3())
    print("\nSorted list:")
    for number in b9:
        print(number)