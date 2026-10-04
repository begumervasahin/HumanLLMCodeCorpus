import pandas as pd
import numpy as np
from arvore import TreeNode, Heap
class class1:
    def fonk1(self, grafo):
        self.b1 = grafo
    def fonk2(self, b10, b11):
        if self.b1.at[b10, b11] == -1:
            return self.b1.at[b11, b10]
        elif self.b1.at[b11, b10] == -1:
            return self.b1.at[b10, b11]
        return min(self.b1.at[b10, b11], self.b1.at[b11, b10])
    def fonk3(self, b10, b11):
        if self.b1.at[b10, b11] == -1 or self.b1.at[b11, b10] == -1:
            return -1
        return max(self.b1.at[b10, b11], self.b1.at[b11, b10])
    def fonk4(self, cidade):
        b2 = np.tril(np.ones(self.b1.shape)).astype(bool)
        b3 = self.b1.where(b2, -1)
        return list(b3[cidade][b3[cidade] > 0].index) + list(b3.loc[cidade][b3.loc[cidade] > 0].index)
def fonk5(b9, b10, b11):
    b4 = TreeNode({"key": b10, "cost": b9.fonk2(b10, b11)})
    b5 = Heap()
    a1 = 0
    while b4.data["key"] != b11:
        b3 = b9.fonk4(b4.data["key"])
        b3 = [
            {
                "key": v,
                "cost": a1 + b9.fonk2(v, b11) + b9.fonk3(b4.Key(), v)
            }
            for v in b3
        ]
        b3 = b4.AddChildren(b3)
        b5.append(b3)
        b6 = b5.pop(lambda x: x.Cost())
        a1 += b9.fonk3(b4.Key(), b6.Key())
        b4 = b6
    b7 = [b4.Key()]
    while b4.father is not None:
        b4 = b4.father
        b7.append(b4.Key())
    b7.reverse()
    return b7
if b8 = = "__main__":
    b9 = class1(pd.read_csv("grafo.csv", index_col=0).fillna(-1).astype(np.float64))
    b10 = input("Cidade de Partida: ")
    b11 = input("Cidade de Destino: ")
    b7 = fonk5(b9, b10, b11)
    print("->".join(b7))