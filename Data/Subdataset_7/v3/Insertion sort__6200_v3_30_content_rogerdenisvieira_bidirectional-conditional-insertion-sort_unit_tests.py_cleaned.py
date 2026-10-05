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
        for b6 in range(low, high):
            if arr[b6] <= b2:
                b3 += 1
                arr[b3], arr[b6] = arr[b6], arr[b3]
        arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
        return b3 + 1
class class2:
    def fonk3(self, arr, left, right):
        if left < right:
            b1 = self.fonk4(arr, left, right)
            self.fonk5(arr, left, b1 - 1)
            self.fonk5(arr, b1 + 1, right)
    def fonk4(self, arr, left, right):
        b2 = arr[right]
        b3 = left
        for b6 in range(left, right):
            if arr[b6] <= b2:
                arr[b3], arr[b6] = arr[b6], arr[b3]
                b3 += 1
        arr[b3], arr[right] = arr[right], arr[b3]
        return b3
class class3:
    def fonk5(self, arr):
        b4 = len(arr)
        for b3 in range(1, b4):
            b5 = arr[b3]
            b6 = b3 - 1
            while b6 >= 0 and b5 < arr[b6]:
                arr[b6 + 1] = arr[b6]
                b6 -= 1
            arr[b6 + 1] = b5
class class4(unittest.TestCase):
    def fonk6(self):
        self.b7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.b8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.b8)
        print(f"Setting things up... Expected: {self.b7} Non-Sorted: {self.b8}")
    def fonk7(self):
        b9 = class2()
        b9.fonk5(self.b8, 0, len(self.b8) - 1)
        self.assertEqual(self.b7, self.b8)
    def fonk8(self):
        b9 = class3()
        b9.fonk5(self.b8)
        self.assertEqual(self.b7, self.b8)
    def fonk9(self):
        b9 = class1()
        b9.fonk5(self.b8, 0, len(self.b8) - 1)
        self.assertEqual(self.b7, self.b8)
    def fonk10(self):
        print()
        self.assertEqual("foo", 1)
if b10 = = '__main__':
    unittest.main()