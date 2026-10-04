
from words import get_text, words
from htable import htable, htable_put, htable_get
def fonk1(b9):
    if not b9:
        return None
    b1 = htable(4011)
    for file_index, file_name in enumerate(b9):
        b2 = words(get_text(file_name))
        for word in b2:
            b3 = htable_get(b1, word)
            if b3 is None:
                htable_put(b1, word, {file_index})
            else:
                b3.add(file_index)
                htable_put(b1, word, b3)
    return b1
def fonk2(b9, b10, terms):
    if not (b9 and b10 and terms):
        return None
    b4 = []
    for term in terms:
        b5 = htable_get(b10, term)
        if b5 is None:
            return []
        b4.append(b5)
    b6 = set.intersection(*b4) if b4 else set()
    b7 = [b9[file_index] for file_index in b6]
    return b7
if b8 = = "__main__":
    b9 = ["file1.txt", "file2.txt", "file3.txt"]
    b10 = fonk1(b9)
    b11 = ["term1", "term2", "term3"]
    b12 = fonk2(b9, b10, b11)
    if b12:
        print("Search Result:")
        for file in b12:
            print(file)
    else:
        print("No results found.")