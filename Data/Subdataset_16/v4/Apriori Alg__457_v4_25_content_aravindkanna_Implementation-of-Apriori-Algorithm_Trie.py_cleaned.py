from queue import Queue
class class1:
    def fonk1(self, b1 = 1, b3="root"):
        self.b2 = {}
        self.b1 = b1
        self.b3 = b3
    def fonk2(self, itemset, b1):
        b4 = self.b2
        for item in itemset:
            if item in b4:
                b4 = b4[item].b2
            else:
                b5 = class1(b1, item)
                b4[item] = b5
                b4 = b5.b2
    def fonk3(self, itemset):
        b4 = self.b2
        for item in itemset:
            if item in b4:
                b4 = b4[item].b2
            else:
                return False
        return True
    def fonk4(self, freq_itemsets, counts):
        for itemset, b1 in zip(freq_itemsets, counts):
            self.fonk2(itemset, b1)
    def fonk5(self, b6 = ""):
        for item, node in self.b2.items():
            b7 = b6 + item
            print(b7)
            node.fonk5(b7 + ",")
    def fonk6(self, b6 = None):
        if b6 is None:
            b6 = []
        for item, node in self.b2.items():
            b8 = b6 + [item]
            yield b8
            yield from node.fonk6(b8)
    def fonk7(self, itemset):
        b4 = self.b2
        for item in itemset:
            b4 = b4[item]
        return b4.b1
