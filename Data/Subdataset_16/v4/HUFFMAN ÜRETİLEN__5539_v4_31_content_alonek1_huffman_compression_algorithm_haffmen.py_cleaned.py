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
        return (self.b6, self.b7)
def fonk3(frequencies):
    b8 = PriorityQueue()
    for char, prob in frequencies.items():
        b8.put((prob, char))
    while b8.qsize() > 1:
        b6, b7 = b8.get(), b8.get()
        b9 = class1(b6, b7)
        b8.put((b6[0] + b7[0], b9))
    return b8.get()
def fonk4(b9, b10 = "", code={}):
    if isinstance(b9[1], class1):
        fonk4(b9[1].b6, b10 + "0", code)
        fonk4(b9[1].b7, b10 + "1", code)
    else:
        code[b9[1]] = b10
    return code
b11 = fonk3(b5)
b12 = fonk4(b11)
print("Character  Probability       Huffman Code")
for char in sorted(b5, b13 = b5.get, reverse=True):
    print(f"{char}         {b5[char]:.10f}     {b12[char]}")
b14 = ''.join(b12[char] for char in b1 if char in b12)
print(f"Encoded b1: {b14}")