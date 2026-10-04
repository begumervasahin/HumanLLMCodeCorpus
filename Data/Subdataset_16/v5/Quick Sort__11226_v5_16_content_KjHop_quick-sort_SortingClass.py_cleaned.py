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
        b2 = arr[len(arr)
        b3 = [number for number in arr if number < b2]
        b4 = [number for number in arr if number == b2]
        b5 = [number for number in arr if number > b2]
        return self.fonk5(b3) + b4 + self.fonk5(b5)
if b6 = = "__main__":
    b7 = class1()
    b8 = [3, 6, 8, 10, 1, 2, 1]
    for number in b8:
        b7.fonk2(number)
    print("Original List:")
    b7.fonk4()
    b9 = b7.fonk5(b7.fonk3())
    print("\nSorted List:")
    for num in b9:
        print(num)