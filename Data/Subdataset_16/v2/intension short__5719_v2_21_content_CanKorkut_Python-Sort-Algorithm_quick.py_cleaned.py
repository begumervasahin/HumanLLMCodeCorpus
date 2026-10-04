import random
def fonk1(size):
    return [random.randint(0, 10000) for _ in range(size)]
b1 = fonk1(10)
b2 = fonk1(100)
b3 = fonk1(1000)
b4 = fonk1(10000)
b5 = list(range(10))
b6 = b5[::-1]
class class1:
    def fonk2(self):
        self.a1 = 0
    def fonk3(self, array, low, high):
        if low < high:
            self.a1 += 1
            b7 = self.fonk4(array, low, high)
            self.fonk3(array, low, b7 - 1)
            self.fonk3(array, b7 + 1, high)
    def fonk4(self, array, low, high):
        b8 = array[high]
        b9 = low - 1
        for j in range(low, high):
            self.a1 += 1
            if array[j] <= b8:
                b9 += 1
                array[b9], array[j] = array[j], array[b9]
        array[b9 + 1], array[high] = array[high], array[b9 + 1]
        return b9 + 1
def fonk5(array):
    print("Original Array:", array)
    b10 = class1()
    b10.fonk3(array, 0, len(array) - 1)
    print("Sorted Array:", array)
    print("Total Comparisons:", b10.a1)
def fonk6():
    fonk5(b2)
if b11 = = "__main__":
    fonk6()