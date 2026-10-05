from collections import Counter
import queue
b1 = open('rand_file').read()
b2 = Counter(b1)
b3 = sum(b2.values())
b4 = {char: b2[char] / b3 for char in b2}
class class1:
    def fonk1(self, b5 = None, b6=None, b7=None):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
def fonk2(b10):
    b8 = queue.PriorityQueue()
    for value in b10:
        b8.put(value)
    while b8.qsize() > 1:
        b5, b6 = b8.get(), b8.get()
        b9 = class1(b5, b6)
        b8.put((b5[0] + b6[0], b9))
    return b8.get()
b10 = [(b4[char], char) for char in b4]
b11 = fonk2(b10)
def fonk3(b9, b12 = "", code={}):
    if isinstance(b9[1].b5[1], class1):
        fonk3(b9[1].b5, b12 + "0", code)
    else:
        code[b9[1].b5[1]] = b12 + "0"
    if isinstance(b9[1].b6[1], class1):
        fonk3(b9[1].b6, b12 + "1", code)
    else:
        code[b9[1].b6[1]] = b12 + "1"
    return code
b13 = fonk3(b11)
for char, probability in sorted(b4.items(), b14 = lambda x: x[1], reverse=True):
    print(char, '{:6.10f}'.format(probability), b13[char])
b15 = "".join(b13[char] for char in b1)
print(b15)