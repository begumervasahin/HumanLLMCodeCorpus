
from words import get_text, words
def fonk1(b8):
    if not b8:
        return None
    b1 = htable(4011)
    for file_index, file_name in enumerate(b8):
        b2 = words(get_text(file_name))
        for word in b2:
            b3 = htable_get(b1, word)
            if b3 is None:
                b3 = set()
            b3.add(file_index)
            htable_put(b1, word, b3)
    return b1
def fonk2(b8, b9, terms):
    if not (b8 and b9 and terms):
        return None
    b4 = []
    b5 = []
    for term in terms:
        b6 = htable_get(b9, term)
        if b6 is None:
            return None
        b5.append(b6)
    b7 = set.intersection(*b5)
    for file_index in b7:
        b4.append(b8[file_index])
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