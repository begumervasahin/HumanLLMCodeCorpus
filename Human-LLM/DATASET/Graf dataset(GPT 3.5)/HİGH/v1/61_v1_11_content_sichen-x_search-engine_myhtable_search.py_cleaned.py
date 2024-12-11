
from words import get_text, words
def fonk1(b8):
    if len(b8) <= 0:
        return None
    b1 = htable(4011)
    for i in range(len(b8)):
        b2 = get_text(b8[i])
        b3 = words(b2)
        for word in b3:
            htable_put(b1, word, set([i]))
    return b1
def fonk2(b8, b9, terms):
    if b8 is None or b9 is None or terms is None or \
            len(b8) == 0 or len(b9) == 0 or len(terms) == 0:
        return None
    b4 = []
    b5 = []
    for term in terms:
        b6 = htable_get(b9, term)
        if b6:
            b5.append(b6)
        else:
            return None
    if len(b5) > 0:
        b7 = set.intersection(*b5)
        for id in b7:
            b4.append(b8[id])
    else:
        return None
    return b4
b8 = ["file1.txt", "file2.txt", "file3.txt"]
b9 = fonk1(b8)
b10 = ["term1", "term2", "term3"]
b11 = fonk2(b8, b9, b10)
if b11:
    print("Search Result:")
    for file in b11:
        print(file)
else:
    print("No results found.")