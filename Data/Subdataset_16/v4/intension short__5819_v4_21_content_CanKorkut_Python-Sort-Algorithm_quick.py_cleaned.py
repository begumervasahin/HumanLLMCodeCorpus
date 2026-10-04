from random import randint
def fonk1(size, b1 = 10000):
    return [randint(0, b1) for _ in range(size)]
b2 = fonk1(10)
b3 = fonk1(100)
b4 = fonk1(1000)
b5 = fonk1(10000)
b6 = list(range(10))
b7 = list(range(9, -1, -1))
class class1:
    def fonk2(self):
        self.a1 = 0
    def fonk3(self, array, low, high):
        if low < high:
            self.a1 += 1
            b8 = self.fonk4(array, low, high)
            self.a1 += 1
            self.fonk3(array, low, b8 - 1)
            self.a1 += 1
            self.fonk3(array, b8 + 1, high)
            self.a1 += 1
    def fonk4(self, array, low, high):
        b9 = array[high]
        self.a1 += 1
        b10 = low - 1
        for j in range(low, high):
            self.a1 += 1
            if array[j] <= b9:
                b10 += 1
                array[b10], array[j] = array[j], array[b10]
                self.a1 += 1
        array[b10 + 1], array[high] = array[high], array[b10 + 1]
        self.a1 += 1
        return b10 + 1
def fonk5(array):
    print("Original array:", array)
    b11 = class1()
    b11.fonk3(array, 0, len(array) - 1)
    print("Sorted array:", array)
    print("QuickSort steps:", b11.a1)
def fonk6():
    fonk5(b3)
if b12 = = "__main__":
    fonk6()