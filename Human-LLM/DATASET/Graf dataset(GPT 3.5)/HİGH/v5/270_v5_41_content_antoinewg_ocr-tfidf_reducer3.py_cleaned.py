import sys
import math
def fonk1(b10, b9, total_docs):
    b1 = b10 / b9
    b2 = math.log(total_docs)
    return b1 * b2
b3 = None
b4 = None
b5 = None
b6 = None
a1 = 0
for b7 in sys.stdin:
    b7 = b7.strip()
    word, b8 = b7.split("\t")
    doc_id, b10, b9 = b8.split(",")
    b10 = int(b10)
    b9 = int(b9)
    if b3 = = word:
        a1 += 1
    else:
        if b3 is not None:
            b11 = fonk1(b5, b6, a1)
            print("(%s,%s)\t%s" % (b3, b4, b11))
        a1 = 1
    b3 = word
    b4 = doc_id
    b5 = b10
    b6 = b9
if b3 is not None:
    b11 = fonk1(b5, b6, a1)
    print("(%s,%s)\t%s" % (b3, b4, b11))