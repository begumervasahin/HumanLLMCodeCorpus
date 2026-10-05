import numpy as np
from path import Path
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        with open(self.b1, 'r') as file:
            b2 = file.read()
            b3 = np.matrix(b2)
        return b3
if b4 = = "__main__":
    b5 = "your_graph_file.txt"
    b6 = class1(b5)
    b3 = b6.fonk2()
    print("Graph Matrix:")
    print(b3)