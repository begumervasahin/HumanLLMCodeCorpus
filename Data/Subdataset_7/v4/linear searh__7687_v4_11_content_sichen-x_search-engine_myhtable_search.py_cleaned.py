from htable import htable_put, htable_get, htable
from words import get_text, words
def fonk1(files):
    if len(files) <= 0:
        return None
    b1 = htable(4011)
    for i in range(len(files)):
        b2 = get_text(files[i])
        b3 = words(b2)
        for word in b3:
            b4 = htable_get(b1, word)
            if b4:
                b4.add(i)
            else:
                htable_put(b1, word, set([i]))
    return b1
def fonk2(files, index, terms):
    if files is None or index is None or terms is None \
        or len(files) == 0 or len(index) == 0 or len(terms) == 0:
        return None
    b5 = []
    b6 = []
    for term in terms:
        b7 = htable_get(index, term)
        if b7:
            b6.append(b7)
        else:
            return None
    if len(b6) > 0:
        b8 = set.intersection(*b6)
        for index in b8:
            b5.append(files[index])
    else:
        return None
    return b5