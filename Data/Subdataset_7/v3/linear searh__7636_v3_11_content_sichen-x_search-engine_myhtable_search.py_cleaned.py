
from words import get_text, words
def fonk1(b7):
    if not b7:
        return None
    b1 = htable(4011)
    for file_index, file_name in enumerate(b7):
        b2 = words(get_text(file_name))
        for word in b2:
            htable_put(b1, word, set([file_index]))
    return b1
def fonk2(b7, b8, terms):
    if not (b7 and b8 and terms):
        return None
    b3 = []
    b4 = []
    for term in terms:
        b5 = htable_get(b8, term)
        if b5 is None:
            return None
        b4.append(b5)
    b6 = set.intersection(*b4)
    for file_index in b6:
        b3.append(b7[file_index])
    return b3
b7 = ["file1.txt", "file2.txt", "file3.txt"]
b8 = fonk1(b7)
b9 = ["term1", "term2", "term3"]
b10 = fonk2(b7, b8, b9)
if b10:
    print("Search Result:")
    for file in b10:
        print(file)
else:
    print("No results found.")