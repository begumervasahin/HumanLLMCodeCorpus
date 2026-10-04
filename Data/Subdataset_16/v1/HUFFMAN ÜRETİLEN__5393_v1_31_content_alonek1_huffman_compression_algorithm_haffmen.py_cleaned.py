from collections import Counter
import queue
def fonk1(b9, b10):
    b1 = Counter(b9)
    b2 = sum(b1[char] for char in b10)
    b3 = {char: b1[char] / b2 for char in b10}
    return b3
class class1:
    def fonk2(self, b4 = None, b5=None):
        self.b4 = b4
        self.b5 = b5
    def fonk3(self):
        return self.b4, self.b5
def fonk4(b11):
    b6 = queue.PriorityQueue()
    for prob, char in b11:
        b6.put((prob, class1(char)))
    while b6.qsize() > 1:
        b4, b5 = b6.get(), b6.get()
        b7 = class1(b4[1], b5[1])
        b6.put((b4[0] + b5[0], b7))
    return b6.get()[1]
def fonk5(b7, b8 = "", code={}):
    if isinstance(b7.b4, class1):
        fonk5(b7.b4, b8 + "0", code)
    else:
        code[b7.b4] = b8 + "0"
    if isinstance(b7.b5, class1):
        fonk5(b7.b5, b8 + "1", code)
    else:
        code[b7.b5] = b8 + "1"
    return code
def fonk6(b9, b13):
    return ''.join(b13[char] for char in b9)
def fonk7():
    b9 = open('rand_file').read()
    b10 = ['A', 'B', 'C', 'D', 'E']
    b3 = fonk1(b9, b10)
    b11 = sorted(b3.items(), b14=lambda item: item[1])
    b12 = fonk4(b11)
    b13 = fonk5(b12)
    for char, prob in sorted(b11, b14 = lambda item: item[1], reverse=True):
        print(f"{char}: {prob:.10f}, Code: {b13[char]}")
    b15 = fonk6(b9, b13)
    print(b15)
if b16 = = "__main__":
    fonk7()