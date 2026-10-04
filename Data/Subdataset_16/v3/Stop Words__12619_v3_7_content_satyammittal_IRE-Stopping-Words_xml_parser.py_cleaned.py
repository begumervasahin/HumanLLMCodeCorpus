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
def fonk2(text):
    b10 = {}
    if text:
        b11 = text.split()
        for word in b11:
            b8[word] = b8.get(word, 0) + 1
            b10[word] = b10.get(word, 0) + 1
    for word in b10:
        b9[word] = b9.get(word, 0) + 1
for b14, elem in etree.iterparse(b3, b12 = ('start', 'end')):
    if len(b9) > 500000:
        break
    b13 = fonk1(elem.b7)
    if b14 = = 'start':
        if b13 = = 'page':
            b4 = ''
            b15 = False
        elif b13 = = 'revision':
            b15 = True
        elif b13 = = 'b4':
            b4 = elem.text
        elif b13 = = 'b16':
            b16 = elem.attrib.get('b4', '')
        elif b13 = = 'text':
            fonk2(elem.text)
b17 = {word: b8[word] * b9[word] for word in b9}
b18 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
a5 = 50
for word, count in b18[:a5]:
    print(f"{word}: {count}")
b19 = time.time() - b5
print(f"Elapsed time: {b19:.2f} seconds")