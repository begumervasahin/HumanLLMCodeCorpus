import random
class class1:
    def fonk1(self, size_of_array, interval_from, interval_to):
        self.b1 = size_of_array
        self.b2 = [random.randint(interval_from, interval_to) for _ in range(size_of_array)]
    def fonk2(self):
        self.b2.clear()
    def fonk3(self):
        print(self.b2)
    def fonk4(self):
        b3 = False
        while not b3:
            b3 = True
            for i in range(self.b1 - 1):
                if self.b2[i] > self.b2[i + 1]:
                    self.b2[i], self.b2[i + 1] = self.b2[i + 1], self.b2[i]
                    b3 = False
def fonk5():
    while True:
        b4 = int(input('Enter size of b2:\b4'))
        b5 = int(input('Enter minimum value for random range:\b4'))
        b6 = int(input('Enter maximum value for random range:\b4'))
        b7 = class1(b4, b5, b6)
        print("Original b2:")
        b7.fonk3()
        b7.fonk4()
        print("Sorted b2:")
        b7.fonk3()
        del b7
if b8 = = "__main__":
    fonk5()