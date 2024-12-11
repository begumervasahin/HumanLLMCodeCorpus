from random import randint
b1 = []
b2 = []
b3 = []
b4 = []
def fonk1(Array, size):
    for _ in range(size):
        Array.append(randint(0, 10000))
fonk1(b1, 10)
fonk1(b2, 100)
fonk1(b3, 1000)
fonk1(b4, 10000)
class class1:
    def fonk2(self):
        self.a1 = 0
    def fonk3(self, array, start, end):
        if start < end:
            b5 = self.fonk4(array, start, end)
            self.fonk3(array, start, b5 - 1)
            self.fonk3(array, b5 + 1, end)
    def fonk4(self, array, start, end):
        b6 = array[end]
        b5 = start - 1
        for j in range(start, end):
            if array[j] <= b6:
                b5 += 1
                array[b5], array[j] = array[j], array[b5]
                self.a1 += 1
        array[b5 + 1], array[end] = array[end], array[b5 + 1]
        self.a1 += 1
        return b5 + 1
def fonk5(array):
    print("Original Array:", array)
    b7 = class1()
    b7.fonk3(array, 0, len(array) - 1)
    print("Sorted Array:", array)
    print("Number of a1:", b7.a1)
def fonk6():
    fonk5(b2)
if b8 = = "__main__":
    fonk6()