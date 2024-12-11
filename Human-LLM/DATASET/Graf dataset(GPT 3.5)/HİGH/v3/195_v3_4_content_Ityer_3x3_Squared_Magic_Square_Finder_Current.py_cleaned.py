import random
import pickle
class class1:
    def fonk1(self):
        self.a1 = 30
        self.a2 = 0
    def fonk2(self):
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        b7 = []
        b8 = []
        b9 = ["Win.txt", "Two.txt", "Three.txt", "Four.txt", "Five.txt", "Six.txt", "Seven.txt"]
        b10 = [b8, b2, b3, b4, b5, b6, b7]
        for filename, b11 in zip(b9, b10):
            with open(filename, 'rb') as f:
                b11 = pickle.load(f)
        return b1, b2, b3, b4, b5, b6, b7, b8
    def fonk3(self):
        b12 = []
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "b16"]:
            b13 = False
            while not b13:
                b14 = random.randint((self.a1 * -1), self.a1)
                if (b14 not in b12) and (b14 < self.a1):
                    b12.append(b14)
                    b13 = True
        return b12
    def fonk4(self, b22, b27, b28, b2, b3, b4, b5, b6, b7, b8, goal):
        a3 = 0
        b15 = max(set(b22), key=b22.count)
        for b16 in b22:
            if b16 = = b15:
                a3 += 1
        if a3 = = 1:
            b28.append(b27)
        elif a3 <= 7:
            b17 = [b2, b3, b4, b5, b6, b7]
            b17[a3 - 2].append(b27)
        else:
            b8.append(b27)
        print(((len(b28)) + sum(len(match) for match in [b2, b3, b4, b5, b6, b7]) + len(b8)), "/", goal)
        return b28, b2, b3, b4, b5, b6, b7, b8
    def fonk5(self, b28, b2, b3, b4, b5, b6, b7, b8, *b27, goal):
        b18 = [b14 ** 2 for b14 in b27]
        b19 = [sum(b18[b16:b16+3]) for b16 in range(0, len(b18), 3)]
        b20 = [sum(b18[b16::3]) for b16 in range(3)]
        b21 = [sum(b18[::4]), sum(b18[2:7:2])]
        b22 = b19 + b20 + b21
        b28, b2, b3, b4, b5, b6, b7, b8 = self.fonk4(b22, b27, b28, b2, b3, b4, b5, b6, b7, b8, goal)
        return b28, b2, b3, b4, b5, b6, b7, b8
    def fonk6(self, lst):
        if lst:
            lst.sort()
            b23 = lst[-1]
            for b16 in range(len(lst) - 2, -1, -1):
                if b23 = = lst[b16]:
                    del lst[b16]
                else:
                    b23 = lst[b16]
        return lst
    def fonk7(self, b28, b2, b3, b4, b5, b6, b7, b8):
        print("Two:", len(b2))
        print("Three:", len(b3))
        print("Four:", len(b4))
        print("Five:", len(b5))
        print("Six:", len(b6))
        print("Seven:", len(b7))
        print("Win:", len(b8))
        print(self.a2, "Duplicates Removed")
        print("Saving Results")
        with open("Win.txt", 'wb') as f:
            pickle.dump(b8, f)
        with open("Two.txt", 'wb') as f:
            pickle.dump(b2, f)
        with open("Three.txt", 'wb') as f:
            pickle.dump(b3, f)
        with open("Four.txt", 'wb') as f:
            pickle.dump(b4, f)
        with open("Five.txt", 'wb') as f:
            pickle.dump(b5, f)
        with open("Six.txt", 'wb') as f:
            pickle.dump(b6, f)
        with open("Seven.txt", 'wb') as f:
            pickle.dump(b7, f)
    def fonk8(self):
        b28, b2, b3, b4, b5, b6, b7, b8 = self.fonk2()
        b24 = len(b28) + sum(len(match) for match in [b2, b3, b4, b5, b6, b7, b8])
        print("Don't run too many tests at once, as b28 are only saved at the end")
        b25 = int(input(f"There are {b24:,d} current tests. How many more? ")) + b24
        b26 = b25 - b24
        while b24 < b25:
            b27 = self.fonk3()
            b28, b2, b3, b4, b5, b6, b7, b8 = self.fonk5(b28, b2, b3, b4, b5, b6, b7, b8, *b27, goal=b25)
            b24 = len(b28) + sum(len(match) for match in [b2, b3, b4, b5, b6, b7, b8])
        print("Before purification:", "{:,d}".format(b24))
        b28 = []
        b2 = self.fonk6(b2)
        b3 = self.fonk6(b3)
        b4 = self.fonk6(b4)
        b5 = self.fonk6(b5)
        b6 = self.fonk6(b6)
        b7 = self.fonk6(b7)
        b8 = self.fonk6(b8)
        b29 = len(b28) + sum(len(match) for match in [b2, b3, b4, b5, b6, b7, b8])
        print("After purification:", "{:,d}".format(b29))
        self.fonk7(b28, b2, b3, b4, b5, b6, b7, b8)
        input("Press enter to close")
if b30 = = "__main__":
    class1().fonk8()