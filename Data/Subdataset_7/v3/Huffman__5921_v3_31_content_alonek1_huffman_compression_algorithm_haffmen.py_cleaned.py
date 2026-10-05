from collections import Counter
import queue
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(b10):
    b1 = Counter(b10)
    b2 = sum(b1.values())
    return {char: count / b2 for char, count in b1.items()}
class class1:
    def fonk3(self, b3 = None, b4=None, b5=None):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
def fonk4(b12):
    b6 = queue.PriorityQueue()
    for value in b12:
        b6.put(value)
    while b6.qsize() > 1:
        b3, b4 = b6.get(), b6.get()
        b7 = class1(b3, b4)
        b6.put((b3[0] + b4[0], b7))
    return b6.get()
def fonk5(b7, b8 = "", code={}):
    b3, b4 = b7[1].b3[1], b7[1].b4[1]
    if isinstance(b3, class1):
        fonk5(b3, b8 + "0", code)
    else:
        code[b3] = b8 + "0"
    if isinstance(b4, class1):
        fonk5(b4, b8 + "1", code)
    else:
        code[b4] = b8 + "1"
    return code
if b9 = = '__main__':
    b10 = fonk1('rand_file')
    b11 = fonk2(b10)
    b12 = [(b11[char], char) for char in b11]
    b13 = fonk4(b12)
    b14 = fonk5(b13)
    for char, probability in sorted(b11.items(), b15 = lambda x: x[1], reverse=True):
        print(char, '{:6.10f}'.format(probability), b14[char])
    b16 = "".join(b14[char] for char in b10)
    print(b16)