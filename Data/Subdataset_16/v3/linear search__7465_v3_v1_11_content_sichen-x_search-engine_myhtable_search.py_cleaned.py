
from htable import htable, htable_put, htable_get
from words import get_text, words
def fonk1(b10):
    if not b10:
        return None
    b1 = htable(4011)
    for i, file in enumerate(b10):
        b2 = get_text(file)
        b3 = words(b2)
        for word in b3:
            b4 = htable_get(b1, word)
            if b4 is None:
                htable_put(b1, word, {i})
            else:
                b4.add(i)
                htable_put(b1, word, b4)
    return b1
def fonk2(b10, b11, terms):
    if not b10 or not b11 or not terms:
        return None
    b5 = []
    for term in terms:
        b6 = htable_get(b11, term)
        if b6:
            b5.append(b6)
        else:
            return None
    if not b5:
        return None
    b7 = set.intersection(*b5)
    b8 = [b10[id] for id in b7]
    return b8
if b9 = = "__main__":
    b10 = ["file1.txt", "file2.txt", "file3.txt"]
    b11 = fonk1(b10)
    b12 = ["term1", "term2", "term3"]
    b13 = fonk2(b10, b11, b12)
    if b13:
        print("Search Result:")
        for file in b13:
            print(file)
    else:
        print("No results found.")