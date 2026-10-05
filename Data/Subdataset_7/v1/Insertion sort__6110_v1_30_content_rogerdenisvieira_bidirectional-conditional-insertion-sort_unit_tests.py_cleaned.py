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
        for b7 in range(low, high):
            if arr[b7] <= b2:
                b3 += 1
                arr[b3], arr[b7] = arr[b7], arr[b3]
        arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
        return b3 + 1
class class2:
    def fonk3(self, arr, l, r):
        if l < r:
            b1 = self.fonk4(arr, l, r)
            self.fonk5(arr, l, b1 - 1)
            self.fonk5(arr, b1 + 1, r)
    def fonk4(self, arr, l, r):
        b4 = arr[r]
        b3 = l
        for b7 in range(l, r):
            if arr[b7] <= b4:
                arr[b3], arr[b7] = arr[b7], arr[b3]
                b3 += 1
        arr[b3], arr[r] = arr[r], arr[b3]
        return b3
class class3:
    def fonk5(self, arr):
        b5 = len(arr)
        for b3 in range(1, b5):
            b6 = arr[b3]
            b7 = b3 - 1
            while b7 >= 0 and b6 < arr[b7]:
                arr[b7 + 1] = arr[b7]
                b7 -= 1
            arr[b7 + 1] = b6
class class4(unittest.TestCase):
    def fonk6(self):
        self.b8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.b9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.b9)
        print("Setting things up... Expected: {0} Non-Sorted: {1}".format(self.b8, self.b9))
    def fonk7(self):
        b10 = class2()
        b10.fonk5(self.b9, 0, len(self.b9) - 1)
        self.assertEqual(self.b8, self.b9)
    def fonk8(self):
        b10 = class3()
        b10.fonk5(self.b9)
        self.assertEqual(self.b8, self.b9)
    def fonk9(self):
        b10 = class1()
        b10.fonk5(self.b9, 0, len(self.b9) - 1)
        self.assertEqual(self.b8, self.b9)
    def fonk10(self):
        print()
        self.assertEqual("foo", 1)
if b11 = = '__main__':
    unittest.main()