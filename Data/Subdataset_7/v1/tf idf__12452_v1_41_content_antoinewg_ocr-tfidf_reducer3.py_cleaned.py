import sys
import math
def fonk1(word_count, word_per_doc, a1, b1 = 2):
    return (word_count / float(word_per_doc)) * math.log(b1 / a1)
b2 = None
b3 = None
b4 = None
b5 = None
a1 = 1
for b6 in sys.stdin:
    b6 = b6.strip()
    word, b7 = b6.split("\t")
    doc_id, b9, b8 = b7.split(",")
    b9 = int(b9)
    b8 = int(b8)
    if b2 = = word:
        a1 += 1
    else:
        if b2 is not None:
            b10 = fonk1(b4, b5, a1)
            print("(%s,%s)\t%s" % (b2, b3, b10))
        a1 = 1
    b2 = word
    b3 = doc_id
    b4 = b9
    b5 = b8
if b2 is not None:
    b10 = fonk1(b4, b5, a1)
    print("(%s,%s)\t%s" % (b2, b3, b10))