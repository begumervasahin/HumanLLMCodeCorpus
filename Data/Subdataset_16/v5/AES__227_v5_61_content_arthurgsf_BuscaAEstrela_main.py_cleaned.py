import pandas as pd
import numpy as np
from arvore import TreeNode, Heap
class class1:
    def fonk1(self, b11):
        self.b1 = b11
    def fonk2(self, b13, b14):
        b2 = self.b1.at[b13, b14]
        b3 = self.b1.at[b14, b13]
        if b2 = = -1 and b3 == -1:
            return -1
        elif b2 = = -1:
            return b3
        elif b3 = = -1:
            return b2
        return min(b2, b3)
    def fonk3(self, b13, b14):
        b2 = self.b1.at[b13, b14]
        b3 = self.b1.at[b14, b13]
        if b2 = = -1 or b3 == -1:
            return -1
        return max(b2, b3)
    def fonk4(self, cidade):
        b4 = self.b1[cidade][self.b1[cidade] > 0].index.tolist()
        b4 += self.b1.loc[cidade][self.b1.loc[cidade] > 0].index.tolist()
        return b4
def fonk5(b12, b13, b14):
    b5 = TreeNode({"key": b13, "cost": b12.fonk2(b13, b14)})
    b6 = Heap()
    a1 = 0
    while b5.data["key"] != b14:
        b4 = b12.fonk4(b5.data["key"])
        b7 = [
            {
                "key": vizinho,
                "cost": a1 + b12.fonk2(vizinho, b14) + b12.fonk3(b5.Key(), vizinho)
            }
            for vizinho in b4
        ]
        b7 = b5.AddChildren(b7)
        b6.append(b7)
        b8 = b6.pop(lambda x: x.Cost())
        a1 += b12.fonk3(b5.Key(), b8.Key())
        b5 = b8
    b9 = [b5.Key()]
    while b5.father is not None:
        b5 = b5.father
        b9.append(b5.Key())
    b9.reverse()
    return b9
if b10 = = "__main__":
    b11 = pd.read_csv("b11.csv", index_col=0).fillna(-1).astype(np.float64)
    b12 = class1(b11)
    b13 = input("Cidade de Partida: ")
    b14 = input("Cidade de Destino: ")
    b9 = fonk5(b12, b13, b14)
    print(" -> ".join(b9))