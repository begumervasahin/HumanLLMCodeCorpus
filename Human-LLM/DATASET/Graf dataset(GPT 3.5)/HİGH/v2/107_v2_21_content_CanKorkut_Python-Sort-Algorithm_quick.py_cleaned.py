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
    def fonk3(self, Array, start, end):
        if start < end:
            b5 = self.fonk4(Array, start, end)
            self.fonk3(Array, start, b5 - 1)
            self.fonk3(Array, b5 + 1, end)
    def fonk4(self, Array, start, end):
        b6 = Array[end]
        b5 = start - 1
        for j in range(start, end):
            if Array[j] <= b6:
                b5 += 1
                Array[b5], Array[j] = Array[j], Array[b5]
        Array[b5 + 1], Array[end] = Array[end], Array[b5 + 1]
        return b5 + 1
def fonk5(Array):
    print("Original Array:", Array)
    b7 = class1()
    b7.fonk3(Array, 0, len(Array) - 1)
    print("Sorted Array:", Array)
    print("Number of comparisons:", b7.a1)
def fonk6():
    fonk5(b2)
if b8 = = "__main__":
    fonk6()