import queue
from collections import Counter
def fonk1(filename):
    with open(filename, 'r') as file:
        return file.read()
def fonk2(b9):
    return Counter(b9)
def fonk3(b10):
    b1 = sum(b10.values())
    return {char: freq / b1 for char, freq in b10.items()}
class class1:
    def fonk4(self, b2 = None, b3=None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk5(self):
        return self.b2, self.b3
def fonk6(b10):
    b5 = queue.PriorityQueue()
    for char, freq in b10.items():
        b5.put((freq, class1(None, None, char)))
    while b5.qsize() > 1:
        b2, b3 = b5.get(), b5.get()
        b6 = class1(b2, b3)
        b5.put((b2[0] + b3[0], b6))
    return b5.get()
def fonk7(b6, b7 = "", code={}):
    if isinstance(b6[1].b2[1], class1):
        fonk7(b6[1].b2, b7 + "0", code)
    else:
        code[b6[1].b2[1]] = b7 + "0"
    if isinstance(b6[1].b3[1], class1):
        fonk7(b6[1].b3, b7 + "1", code)
    else:
        code[b6[1].b3[1]] = b7 + "1"
    return code
def fonk8(b9, code):
    return ''.join(code[char] for char in b9)
if b8 = = '__main__':
    b9 = fonk1('rand_file')
    b10 = fonk2(b9)
    b11 = fonk3(b10)
    b12 = fonk6(b11)
    b13 = fonk7(b12)
    for char, freq in sorted(b11.items(), b14 = lambda x: x[1], reverse=True):
        print(char, '{:.10f}'.format(freq), b13[char])
    b15 = fonk8(b9, b13)
    print(b15)