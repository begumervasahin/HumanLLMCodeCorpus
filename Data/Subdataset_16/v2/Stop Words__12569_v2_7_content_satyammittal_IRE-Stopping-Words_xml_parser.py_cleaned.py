import xml.etree.ElementTree as etree
import time
import os
import operator
b1 = ''
b2 = 'idwiki-20170801-pages-meta-current.xml'
b3 = os.path.join(b1, b2)
a1 = 0
a2 = 0
a3 = 0
a4 = 0
b4 = None
b5 = time.time()
def fonk1(b7):
    b6 = b7.rfind("}")
    if b6 != -1:
        b7 = b7[b6 + 1:]
    return b7
b8 = {}
b9 = {}
b10 = {}
for b13, elem in etree.iterparse(b3, b11 = ('start', 'end')):
    b10 = {}
    if len(b9) > 500000:
        break
    b12 = fonk1(elem.b7)
    if b13 = = 'start':
        if b12 = = 'page':
            b4 = ''
            b14 = False
        elif b12 = = 'revision':
            b14 = True
        else:
            if b12 = = 'b4':
                b4 = elem.b16
            elif b12 = = 'b15':
                b15 = elem.attrib.get('b4', '')
            elif b12 = = 'b16':
                b16 = elem.b16
                if b16:
                    b17 = b16.split()
                    for word in b17:
                        b8[word] = b8.get(word, 0) + 1
                        b10[word] = b10.get(word, 0) + 1
        for word in b10:
            b9[word] = b9.get(word, 0) + 1
b18 = {word: b8[word] * b9[word] for word in b9}
b19 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
a5 = 50
for word, count in b19[:a5]:
    print(f"{word}: {count}")
b20 = time.time() - b5
print(f"Elapsed time: {b20:.2f} seconds")