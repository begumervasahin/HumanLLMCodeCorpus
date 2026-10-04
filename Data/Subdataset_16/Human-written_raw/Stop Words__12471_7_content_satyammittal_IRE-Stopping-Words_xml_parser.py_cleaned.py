import xml.etree.ElementTree as etree
import codecs
import csv
import time
import os
import operator
b1 = ''
b2 = 'hiwiki.xml'
b2 = 'idwiki-20170801-pages-meta-current.xml'
b3 = os.path.join(b1, b2)
a1 = 0
a2 = 0
a3 = 0
a4 = 0
b4 = None
b5 = time.time()
def fonk1(b6):
    b6 = elem.tag
    b7 = k = b6.rfind("}")
    if b7 != -1:
        b6 = b6[b7 + 1:]
    return b6
b8 = {}
a5 = 0
b9 = {}
b10 = {}
for b13, elem in etree.iterparse(b3, b11 = ('start', 'end')):
    a5 += 1
    b9 = {}
    if a5 > 500000:
        break
    b12 = fonk1(elem.tag)
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
                if b16 != None:
                    for word in b16.split():
                        if word in b8:
                            b8[word]+=1
                        else:
                            b8[word]=1
                        if word in b9:
                            b9[word]+=1
                        else:
                            b9[word]=1
        for a in b9:
            if a in b10:
                b10[a]+=1
            else:
                b10[a]=1
b17 = {}
for a in b10:
    b17[a]=b8[a]*b10[a]
b18 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
a5 = 50
for d in b18:
    a5-=1
    if a5<0:
        break
    print d[0],':',d[1]