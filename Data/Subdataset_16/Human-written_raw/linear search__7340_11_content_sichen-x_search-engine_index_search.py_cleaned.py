from collections import defaultdict
from words import get_text, words
def fonk1(b4):
    if len(b4) <= 0:
        return None
    b1 = defaultdict(set)
    for i in range(len(b4)):
        b2 = get_text(b4[i])
        b3 = words(b2)
        for word in b3:
            b1[word].add(i)
    return b1
def fonk2(b4, b1, terms):
    if b4 = = None or b1 == None or terms == None or \
        len(b4) == 0 or len(b1) == 0 or len(terms) == 0:
        return None
    b5 = []
    b6 = []
    for term in terms:
        b7 = b1.get(term)
        if b7:
            b6.append(b1[term])
        else:
            return None
    if len(b6) > 0:
        b8 = set.intersection(*b6)
        for id in b8:
            b5.append(b4[id])
    else:
        return None
    return b5