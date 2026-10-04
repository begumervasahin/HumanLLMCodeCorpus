import unittest
import random
class class1:
    def fonk1(self, arr, low, high):
        if low < high:
            b1 = self.fonk4(arr, low, high)
            self.fonk5(arr, low, b1 - 1)
            self.fonk5(arr, b1 + 1, high)
    def fonk2(self, arr, low, high):
        b2 = arr[high]
        b3 = low - 1
        for b5 in range(low, high):
            if arr[b5] <= b2:
                b3 += 1
                arr[b3], arr[b5] = arr[b5], arr[b3]
        arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
        return b3 + 1
class class2:
    def fonk3(self, arr, low, high):
        if low < high:
            b1 = self.fonk4(arr, low, high)
            self.fonk5(arr, low, b1 - 1)
            self.fonk5(arr, b1 + 1, high)
    def fonk4(self, arr, low, high):
        b2 = arr[high]
        b3 = low - 1
        for b5 in range(low, high):
            if arr[b5] <= b2:
                b3 += 1
                arr[b3], arr[b5] = arr[b5], arr[b3]
        arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
        return b3 + 1
class class3:
    def fonk5(self, arr):
        for b3 in range(1, len(arr)):
            b4 = arr[b3]
            b5 = b3 - 1
            while b5 >= 0 and arr[b5] > b4:
                arr[b5 + 1] = arr[b5]
                b5 -= 1
            arr[b5 + 1] = b4
class class4(unittest.TestCase):
    def fonk6(self):
        self.b6 = list(range(10))
        self.b7 = self.b6[:]
        random.shuffle(self.b7)
        print(f"Setup complete. Expected: {self.b6}, Non-Sorted: {self.b7}")
    def fonk7(self):
        b8 = class1()
        b8.fonk5(self.b7, 0, len(self.b7) - 1)
        self.assertEqual(self.b6, self.b7)
    def fonk8(self):
        b8 = class2()
        b8.fonk5(self.b7, 0, len(self.b7) - 1)
        self.assertEqual(self.b6, self.b7)
    def fonk9(self):
        b8 = class3()
        b8.fonk5(self.b7)
        self.assertEqual(self.b6, self.b7)
    def fonk10(self):
        self.assertEqual("foo", 1)
if b9 = = '__main__':
    unittest.main()