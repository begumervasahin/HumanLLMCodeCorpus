import pandas as pd
import itertools
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = 0.01, min_confidence=0.01):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b1
        self.b5 = min_confidence
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.fonk10()
    def fonk2(self, product_freq):
        return product_freq / self.b6 >= self.b4, product_freq / self.b6
    def fonk3(self, b32, b18):
        return b32 / b18 >= self.b5, b32 / b18
    def fonk4(self, itemset, a1):
        b10 = []
        b11 = []
        b12 = len(itemset)
        for i in range(b12):
            for j in range(i + 1, b12):
                b13 = itemset[i]
                b14 = itemset[j]
                b13.sort()
                b14.sort()
                if b13 != b14:
                    b10.append(b13 + list(set(b14) - set(b13)))
        b15 = set(tuple(row) for row in b10)
        b16 = [list(b33) for b33 in b15]
        for b33 in b16:
            if len(b33) == a1:
                b11.append(b33)
        return b11
    def fonk5(self):
        b17 = []
        for b35 in self.b8:
            item_support_status, b18 = self.fonk2(self.b8[b35])
            if item_support_status:
                b17.append([b35])
        return b17
    def fonk6(self):
        a1 = 1
        b19 = self.fonk5()
        b20 = []
        while a1 < 2:
            a1 += 1
            b21 = self.fonk4(itemset=b19, a1=a1)
            for b33 in b21:
                b22 = []
                a2 = 0
                b23 = set(b33)
                for order_data in self.b7:
                    if b23.issubset(order_data):
                        a2 += 1
                item_support_status, b18 = self.fonk2(a2)
                if item_support_status:
                    b33.sort()
                    b22.append([b33, b18])
                if len(b22) != 0:
                    b19 = []
                    b19 = b22
                    b20.append(b22)
        return b20
    def fonk7(self, b29, b26):
        print("Items added to b26:")
        print(b26)
        b24 = input("Do you want to add more items? Press Y for Yes or N for Checkout\b42")
        if b24.lower() == 'y':
            self.fonk8(b29, b26)
        else:
            print("Thank you for shopping with us.")
    def fonk8(self, b29, b25 = []):
        b26 = b25
        while True:
            b27 = input("Please choose an b33 you want to buy, or press 'Q' to quit\b42")
            if b27.lower() == 'q':
                break
            else:
                if b27 in b29:
                    print("These items are bought together often. Do you want any of these?")
                    print(b29[b27])
                    b26.append(b27)
                else:
                    print(f"{b27} not found")
        self.fonk7(b29, b26)
    def fonk9(self):
        print("Association Rules")
        print("-----------------")
        print("RULES \t\t SUPPORT \t\t CONFIDENCE")
        b28 = self.fonk6()
        b29 = dict()
        a3 = 1
        a4 = 1
        for pair_list in b28:
            for pair in pair_list:
                b30 = pair[:-1]
                for b33 in b30:
                    b30 = b33
                b31 = set(itertools.combinations(b30, a3))
                b32 = pair[-1]
                for b33 in b31:
                    a2 = 0
                    b33 = set(b33)
                    for order_data in self.b7:
                        if b33.issubset(order_data):
                            a2 += 1
                    item_support_status, b18 = self.fonk2(a2)
                    pair_confidence_status, b34 = self.fonk3(b32, b18)
                    if pair_confidence_status:
                        for i in b30:
                            if i not in b33:
                                b35 = i
                        b33 = list(b33)
                        if b33[0] in b29:
                            b36 = b29.get(b33[0])
                            b36.append(b35)
                        else:
                            b29[b33[0]] = [b35]
                        print(f"Rule
                        a4 += 1
        b26 = []
        self.fonk8(b29, b26)
    def fonk10(self):
        b37 = pd.read_csv(self.b2)
        b38 = pd.read_csv(self.b3)
        b39 = b37[['order_id', 'product_id']]
        b38 = b38[['product_id', 'product_name']]
        b40 = b38.set_index('product_id')['product_name']
        b41 = defaultdict(list)
        for index, row in b39.head(b42 = 100000).iterrows():
            b41[row[0]].append(b40[row[1]].replace(" ", ""))
        a5 = 0
        b43 = {}
        b7 = []
        for key, value in b41.items():
            b16 = []
            a5 += 1
            for b44 in value:
                b44 = b44.replace(" ", "")
                b16.append(b44)
                if b44 not in b43.keys():
                    b43[b44] = 1
                else:
                    b43[b44] += 1
            b7.append(b16)
        self.b6 = a5
        self.b7 = [set(transaction_items) for transaction_items in b7]
        self.b8 = b43
        self.b9 = b41
if b45 = = "__main__":
    a6 = 1
    a7 = 10
    b2 = 'https:
    b3 = 'https:
    b46 = class1(b2=b2, b3=b3,
                                 b1 = a6 / 100, min_confidence=a7 / 100)
    b46.fonk9()