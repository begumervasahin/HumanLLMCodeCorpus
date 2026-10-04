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
        b2 = arr[len(arr) - 1]
        b3 = [number for number in arr if number < b2]
        b4 = [number for number in arr if number == b2]
        b5 = [number for number in arr if number > b2]
        return self.fonk5(b3) + b4 + self.fonk5(b5)
if b6 = = "__main__":
    b7 = class1()
    b7.fonk2(3)
    b7.fonk2(6)
    b7.fonk2(8)
    b7.fonk2(10)
    b7.fonk2(1)
    b7.fonk2(2)
    b7.fonk2(1)
    print("Original List:")
    b7.fonk4()
    b8 = b7.fonk5(b7.fonk3())
    print("\nSorted List:")
    for num in b8:
        print(num)