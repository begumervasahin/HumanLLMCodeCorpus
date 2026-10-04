from collections import Counter
from queue import PriorityQueue
with open('rand_file') as file:
    b1 = file.read()
b2 = Counter(b1)
b3 = ['A', 'B', 'C', 'D', 'E']
b4 = sum(b2[char] for char in b3)
b5 = {char: b2[char] / b4 for char in b3}
class class1:
    def fonk1(self, b6 = None, b7=None):
        self.b6 = b6
        self.b7 = b7
    def fonk2(self):
        return self.b6, self.b7
def fonk3(b5):
    b8 = PriorityQueue()
    for char, prob in b5.items():
        b8.put((prob, char))
    while b8.qsize() > 1:
        left_node, b9 = b8.get(), b8.get()
        b10 = class1(left_node, b9)
        b8.put((left_node[0] + b9[0], b10))
    return b8.get()
def fonk4(b10, b11 = "", b12=None):
    if b12 is None:
        b12 = {}
    if isinstance(b10[1], class1):
        fonk4(b10[1].b6, b11 + "0", b12)
        fonk4(b10[1].b7, b11 + "1", b12)
    else:
        b12[b10[1]] = b11
    return b12
b13 = fonk3(b5)
b14 = fonk4(b13)
print("Character  Probability       Huffman Code")
for char in sorted(b5, b15 = b5.get, reverse=True):
    print(f"{char}         {b5[char]:.10f}     {b14[char]}")
b16 = ''.join(b14[char] for char in b1 if char in b14)
print(f"Encoded b1: {b16}")