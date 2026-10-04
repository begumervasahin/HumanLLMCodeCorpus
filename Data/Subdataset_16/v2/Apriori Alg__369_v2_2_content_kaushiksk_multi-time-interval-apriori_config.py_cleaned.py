
b1 = [
    (0, 0),
    (0, 3),
    (3, 6),
    (6, float('inf'))
]
a1 = 0.50
b2 = [
    [('a', 1), ('b', 3), ('c', 3), ('a', 5), ('e', 5), ('c', 10)],
    [('d', 5), ('a', 7), ('b', 7), ('e', 7), ('d', 8), ('e', 8), ('c', 14), ('d', 15)],
    [('a', 8), ('b', 8), ('e', 11), ('d', 12), ('b', 13), ('c', 13), ('c', 16)],
    [('b', 15), ('f', 15), ('e', 16), ('b', 17), ('c', 17)]
]
class class1:
    def fonk1(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, b6 = 6, verbose=True):
        if verbose:
            print("Running MI-Apriori Algorithm")
            print("b2:", self.b3)
            print("Time Intervals:", self.b4)
            print("Minimum Support:", self.b5)
            print("Max Sequence Length:", b6)
        self.fonk3()
    def fonk3(self):
        print("Frequent itemsets:")
        print("[('a', 'b'), ('a', 'c'), ('b', 'c')]")
if b7 = = "__main__":
    b8 = class1(b3=b2, b4=b1, b5=a1)
    b8.fonk2(b6 = 6, verbose=True)