import pandas as pd
import itertools
from collections import defaultdict
a1 = 100000
class class1:
    def fonk1(self, b2, b3, b1 = 0.01, b44=0.01):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b1
        self.b5 = b44
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.fonk10()
    def fonk2(self, product_freq):
        return product_freq / self.b6 >= self.b4, product_freq / self.b6
    def fonk3(self, b29, b16):
        return b29 / b16 >= self.b5, b29 / b16
    def fonk4(self, b17, a2):
        b10 = []
        b11 = len(b17)
        for i in range(b11):
            for j in range(i + 1, b11):
                b12 = b17[i]
                b13 = b17[j]
                b14 = b12 + list(set(b13) - set(b12))
                b14.sort()
                if b14 not in b10:
                    b10.append(b14)
        return [b30 for b30 in b10 if len(b30) == a2]
    def fonk5(self):
        b15 = []
        for b32 in self.b8:
            item_support_status, b16 = self.fonk2(self.b8[b32])
            if item_support_status:
                b15.append([b32])
        return b15
    def fonk6(self):
        a2 = 1
        b17 = self.fonk5()
        b18 = []
        while a2 < 2:
            a2 += 1
            b19 = self.fonk4(b17=b17, a2=a2)
            b20 = []
            for b30 in b19:
                b21 = sum(1 for order_data in self.b7 if set(b30).issubset(order_data))
                item_support_status, b16 = self.fonk2(b21)
                if item_support_status:
                    b30.sort()
                    b20.append([b30, b16])
            if b20:
                b17 = b20
                b18.append(b20)
        return b18
    def fonk7(self, b27, b24):
        print("Items added to b24:")
        print(b24)
        b22 = input("Do you want to add more items? Press Y for Yes or N for Checkout\b38")
        if b22.lower() == 'y':
            self.fonk8(b27, b24)
        else:
            print("Thank you for shopping with us.")
    def fonk8(self, b27, b23 = []):
        b24 = b23
        while True:
            b25 = input("Please choose an b30 you want to buy, or press 'Q' to quit\b38")
            if b25.lower() == 'q':
                break
            else:
                if b25 in b27:
                    print("These items are bought together often. Do you want any of these?")
                    print(b27[b25])
                    b24.append(b25)
                else:
                    print(f"{b25} not found")
        self.fonk7(b27, b24)
    def fonk9(self):
        print("Association Rules")
        print("-----------------")
        print("RULES \t\t SUPPORT \t\t CONFIDENCE")
        b26 = self.fonk6()
        b27 = defaultdict(list)
        a3 = 1
        for pair_list in b26:
            for pair in pair_list:
                b28 = pair[:-1]
                a4 = 1
                for b30 in b28:
                    b28 = b30
                b29 = pair[-1]
                for b30 in itertools.combinations(b28, a4):
                    b30 = set(b30)
                    b21 = sum(1 for order_data in self.b7 if b30.issubset(order_data))
                    item_support_status, b16 = self.fonk2(b21)
                    if item_support_status:
                        pair_confidence_status, b31 = self.fonk3(b29, b16)
                        if pair_confidence_status:
                            for i in b28:
                                if i not in b30:
                                    b32 = i
                            b30 = list(b30)
                            b27[b30[0]].append(b32)
                            print(f"Rule
                            a3 += 1
        b24 = []
        self.fonk8(b27, b24)
    def fonk10(self):
        b33 = pd.read_csv(self.b2)
        b34 = pd.read_csv(self.b3)
        b35 = b33[['order_id', 'product_id']]
        b34 = b34[['product_id', 'product_name']]
        b36 = b34.set_index('product_id')['product_name']
        b37 = defaultdict(list)
        for index, row in b35.head(b38 = a1).iterrows():
            b37[row[0]].append(b36[row[1]].replace(" ", ""))
        a5 = 0
        b39 = {}
        b7 = []
        for key, value in b37.items():
            b40 = []
            a5 += 1
            for b41 in value:
                b41 = b41.replace(" ", "")
                b40.append(b41)
                if b41 not in b39.keys():
                    b39[b41] = 1
                else:
                    b39[b41] += 1
            b7.append(b40)
        self.b6 = a5
        self.b7 = [set(transaction_items) for transaction_items in b7]
        self.b8 = b39
        self.b9 = b37
if b42 = = "__main__":
    a6 = 1
    a7 = 10
    b2 = 'https:
    b3 = 'https:
    b43 = class1(
        b2 = b2,
        b3 = b3,
        b1 = a6 / 100,
        b44 = a7 / 100
    )
    b43.fonk9()