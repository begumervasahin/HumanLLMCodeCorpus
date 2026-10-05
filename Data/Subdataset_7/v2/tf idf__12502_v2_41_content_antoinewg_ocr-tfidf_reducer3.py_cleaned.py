import sys
import math
def fonk1(b11, b10, a1, b1 = 2):
    b2 = b11 / float(b10)
    b3 = math.log(b1 / a1)
    return b2 * b3
b4 = None
b5 = None
b6 = None
b7 = None
a1 = 1
for b8 in sys.stdin:
    b8 = b8.strip()
    word, b9 = b8.split("\t")
    doc_id, b11, b10 = b9.split(",")
    b11 = int(b11)
    b10 = int(b10)
    if b4 = = word:
        a1 += 1
    else:
        if b4 is not None:
            b12 = fonk1(b6, b7, a1)
            print("(%s,%s)\t%s" % (b4, b5, b12))
        a1 = 1
    b4 = word
    b5 = doc_id
    b6 = b11
    b7 = b10
if b4 is not None:
    b12 = fonk1(b6, b7, a1)
    print("(%s,%s)\t%s" % (b4, b5, b12))