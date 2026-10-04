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
a5 = 0
for b13, elem in etree.iterparse(b3, b10 = ('start', 'end')):
    a5 += 1
    b11 = {}
    if a5 > 500000:
        break
    b12 = fonk1(elem.b7)
    if b13 = = 'start':
        if b12 = = 'page':
            b4 = ''
            a6 = -1
            b14 = ''
            b15 = False
            a7 = 0
        elif b12 = = 'revision':
            b15 = True
        else:
            if b12 = = 'b4':
                b4 = elem.b16
            elif b12 = = 'b14':
                b14 = elem.attrib['b4']
            elif b12 = = 'b16':
                b16 = elem.b16
                if b16 is not None:
                    for word in b16.split():
                        b8[word] = b8.get(word, 0) + 1
                        b11[word] = b11.get(word, 0) + 1
        for word in b11:
            b9[word] = b9.get(word, 0) + 1
b17 = {word: b8[word] * b9[word] for word in b9}
b18 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
a8 = 50
for word, count in b18[:a8]:
    print(f"{word}: {count}")
print(f"Processing time: {time.time() - b5:.2f} seconds")