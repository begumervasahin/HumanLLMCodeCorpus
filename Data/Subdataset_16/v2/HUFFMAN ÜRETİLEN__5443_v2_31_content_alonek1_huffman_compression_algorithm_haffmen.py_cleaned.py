from collections import Counter
import queue
def fonk1(b11, b12):
    b1 = Counter(b11)
    b2 = sum(b1[char] for char in b12)
    return {char: b1[char] / b2 for char in b12}
class class1:
    def fonk2(self, b3 = None, b4=None):
        self.b3 = b3
        self.b4 = b4
    def fonk3(self):
        return self.b3, self.b4
def fonk4(b14):
    b5 = queue.PriorityQueue()
    for prob, char in b14:
        b5.put((prob, class1(char)))
    while b5.qsize() > 1:
        left_prob, b6 = b5.get()
        right_prob, b7 = b5.get()
        b8 = class1(b6, b7)
        b5.put((left_prob + right_prob, b8))
    return b5.get()[1]
def fonk5(node, b9 = "", b10=None):
    if b10 is None:
        b10 = {}
    if isinstance(node.b3, class1):
        fonk5(node.b3, b9 + "0", b10)
    else:
        b10[node.b3] = b9 + "0"
    if isinstance(node.b4, class1):
        fonk5(node.b4, b9 + "1", b10)
    else:
        b10[node.b4] = b9 + "1"
    return b10
def fonk6(b11, b16):
    return ''.join(b16[char] for char in b11)
def fonk7():
    with open('rand_file', 'r') as file:
        b11 = file.read()
    b12 = ['A', 'B', 'C', 'D', 'E']
    b13 = fonk1(b11, b12)
    b14 = sorted(b13.items(), b17=lambda item: item[1])
    b15 = fonk4(b14)
    b16 = fonk5(b15)
    for char, prob in sorted(b14, b17 = lambda item: item[1], reverse=True):
        print(f"{char}: {prob:.10f}, Code: {b16[char]}")
    b18 = fonk6(b11, b16)
    print(b18)
if b19 = = "__main__":
    fonk7()