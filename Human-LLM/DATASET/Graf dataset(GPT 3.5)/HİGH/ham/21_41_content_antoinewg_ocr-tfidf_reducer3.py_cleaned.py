from operator import itemgetter
import sys
import math
b1 = None
b2 = None
b3 = None
b4 = None
a1 = 1
def fonk1(word_count, word_per_doc, a1, b5 = 2):
    return (word_count / float(word_per_doc)) * math.log(b5 / a1)
for b6 in sys.stdin:
    b6 = b6.strip()
    word, b7 = b6.split("\t")
    doc_id, b9, b8 = b7.split(",")
    b9 = int(b9)
    b8 = int(b8)
    if b1 = = word:
        a1 = 2
        b10 = fonk1(b3, b4, a1)
        print("(%s,%s)\t%s" % (b1, b2, b10))
    else:
        if b1 is not None:
            b10 = fonk1(b3, b4, a1)
            print("(%s,%s)\t%s" % (b1, b2, b10))
    b1 = word
    b2 = doc_id
    b3 = b9
    b4 = b8
    a1 = 1
b10 = fonk1(b3, b4, a1)
print("(%s,%s)\t%s" % (b1, b2, b10))