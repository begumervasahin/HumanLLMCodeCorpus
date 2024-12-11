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
    def fonk3(self, b29, b15):
        return b29 / b15 >= self.b5, b29 / b15
    def fonk4(self, itemset, a1):
        b10 = []
        b11 = len(itemset)
        for i in range(b11):
            for j in range(i + 1, b11):
                b12 = itemset[i]
                b13 = itemset[j]
                b12.sort()
                b13.sort()
                if b12 != b13:
                    b10.append(b12 + list(set(b13) - set(b12))))
        return [item for item in b10 if len(item) == a1]
    def fonk5(self):
        b14 = []
        for b31, freq in self.b8.items():
            item_support_status, b15 = self.fonk2(freq)
            if item_support_status:
                b14.append([b31])
        return b14
    def fonk6(self):
        a1 = 1
        b16 = self.fonk5()
        b17 = []
        while a1 < 2:
            a1 += 1
            b18 = self.fonk4(itemset=b16, a1=a1)
            b19 = []
            for item in b18:
                b20 = sum(1 for order_data in self.b7 if set(item).issubset(order_data))
                item_support_status, b15 = self.fonk2(b20)
                if item_support_status:
                    item.sort()
                    b19.append([item, b15])
            if b19:
                b16 = b19
                b17.append(b19)
        return b17
    def fonk7(self, b26, b23):
        print("Items added to b23:")
        print(b23)
        b21 = input("Do you want to add more items? Press Y for Yes or N for Checkout\b37")
        if b21.lower() == 'y':
            self.fonk8(b26, b23)
        else:
            print("Thank you for shopping with us.")
    def fonk8(self, b26, b22 = []):
        b23 = b22
        while True:
            b24 = input("Please choose an item you want to buy, or press 'Q' to quit\b37").lower()
            if b24 = = 'q':
                break
            else:
                if b24 in b26:
                    print("These items are bought together often. Do you want any of these?")
                    print(b26[b24])
                    b23.append(b24)
                else:
                    print(f"{b24} not found")
        self.fonk7(b26, b23)
    def fonk9(self):
        print("Association Rules")
        print("-----------------")
        print("RULES \t\t SUPPORT \t\t CONFIDENCE")
        b25 = self.fonk6()
        b26 = defaultdict(list)
        a2 = 1
        for pair_list in b25:
            for pair in pair_list:
                b27 = pair[:-1]
                a3 = 1
                for item in b27:
                    b27 = item
                b28 = set(itertools.combinations(b27, a3))
                b29 = pair[-1]
                for item in b28:
                    b20 = sum(1 for order_data in self.b7 if set(item).issubset(order_data))
                    item_support_status, b15 = self.fonk2(b20)
                    pair_confidence_status, b30 = self.fonk3(b29, b15)
                    if pair_confidence_status:
                        b31 = next(i for i in b27 if i not in item)
                        b26[item[0]].append(b31)
                        print(f"Rule
                        a2 += 1
        b23 = []
        self.fonk8(b26, b23)
    def fonk10(self):
        b32 = pd.read_csv(self.b2)
        b33 = pd.read_csv(self.b3)
        b34 = b32[['order_id', 'product_id']]
        b33 = b33[['product_id', 'product_name']]
        b35 = b33.set_index('product_id')['product_name']
        b36 = defaultdict(list)
        for index, row in b34.head(b37 = 100000).iterrows():
            b36[row[0]].append(b35[row[1]].replace(" ", ""))
        a4 = 0
        b38 = {}
        b7 = []
        for key, value in b36.items():
            b39 = []
            a4 += 1
            for b40 in value:
                b40 = b40.replace(" ", "")
                b39.append(b40)
                if b40 not in b38:
                    b38[b40] = 1
                else:
                    b38[b40] += 1
            b7.append(b39)
        self.b6 = a4
        self.b7 = [set(transaction_items) for transaction_items in b7]
        self.b8 = b38
        self.b9 = b36
if b41 = = "__main__":
    a5 = 1
    a6 = 10
    b2 = 'https:
    b3 = 'https:
    b42 = class1(b2=b2, b3=b3,
                                 b1 = a5 / 100, min_confidence=a6 / 100)
    b42.fonk9()