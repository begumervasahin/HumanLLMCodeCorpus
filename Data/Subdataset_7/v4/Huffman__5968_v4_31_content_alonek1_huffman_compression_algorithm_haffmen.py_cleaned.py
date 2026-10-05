from collections import Counter
import queue
b1 = open('rand_file').read()
b2 = Counter(b1)
b3 = b2['A'] + b2['B'] + b2['C'] + b2['D'] + b2['E']
b4 = b2['A'] / b3
b5 = b2['B'] / b3
b6 = b2['C'] / b3
b7 = b2['D'] / b3
b8 = b2['E'] / b3
class class1(object):
    def fonk1(self, b9 = None, b10=None, b11=None):
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
    def fonk2(self):
        return((self.b9, self.b10))
b12 = [(b4, 'A'), (b5, 'B'), (b6, 'C'), (b7, 'D'),(b8, 'E') ]
def fonk3(frequencies):
    b13 = queue.PriorityQueue()
    for value in frequencies:
        b13.put(value)
    while b13.qsize() > 1:
        l, b14 = b13.get(), b13.get()
        b15 = class1(l, b14)
        b13.put((l[0] + b14[0], b15))
    return b13.get()
b15 = fonk3(b12)
def fonk4(b15, b16 = "", b17={}):
    if isinstance(b15[1].b9[1], class1):
        fonk4(b15[1].b9, b16 + "0", b17)
    else:
        b17[b15[1].b9[1]] = b16 + "0"
    if isinstance(b15[1].b10[1], class1):
        fonk4(b15[1].b10, b16 + "1", b17)
    else:
        b17[b15[1].b10[1]] = b16 + "1"
    return(b17)
b17 = fonk4(b15)
for i in sorted(b12, b18 = True):
    print(i[1], '{:6.10f}'.format(i[0]), b17[i[1]])
b19 = ""
for b20 in b1:
    if b20 = = 'A':
        b19 += b17['A']
    elif b20 = = 'B':
        b19 += b17['B']
    elif b20 = = 'C':
        b19 += b17['C']
    elif b20 = = 'D':
        b19 += b17['D']
    else:
        b19 += b17['E']
print(b19)