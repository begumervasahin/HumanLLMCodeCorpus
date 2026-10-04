from collections import Counter
from queue import PriorityQueue
def fonk1(b12, b13):
    b1 = Counter(b12)
    b2 = sum(b1[b3] for b3 in b13)
    return {b3: b1[b3] / b2 for b3 in b13}
class class1:
    def fonk2(self, b3 = None, b4=None, b5=None):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk3(self):
        return self.b3 is not None
def fonk4(b15):
    b6 = PriorityQueue()
    for b3, prob in b15:
        b6.put((prob, class1(b3 = b3)))
    while b6.qsize() > 1:
        left_prob, b7 = b6.get()
        right_prob, b8 = b6.get()
        b9 = class1(b4=b7, b5=b8)
        b6.put((left_prob + right_prob, b9))
    return b6.get()[1]
def fonk5(node, b10 = "", b11=None):
    if b11 is None:
        b11 = {}
    if node.fonk3():
        b11[node.b3] = b10
    else:
        fonk5(node.b4, b10 + "0", b11)
        fonk5(node.b5, b10 + "1", b11)
    return b11
def fonk6(b12, b17):
    return ''.join(b17[b3] for b3 in b12)
def fonk7():
    with open('rand_file', 'r') as file:
        b12 = file.read()
    b13 = ['A', 'B', 'C', 'D', 'E']
    b14 = fonk1(b12, b13)
    b15 = sorted(b14.items(), b18=lambda item: item[1])
    b16 = fonk4(b15)
    b17 = fonk5(b16)
    print("Character Frequencies and Huffman Codes:")
    for b3, prob in sorted(b15, b18 = lambda item: item[1], reverse=True):
        print(f"Character: {b3}, Probability: {prob:.10f}, Code: {b17[b3]}")
    b19 = fonk6(b12, b17)
    print("\nEncoded Text:")
    print(b19)
if b20 = = "__main__":
    fonk7()