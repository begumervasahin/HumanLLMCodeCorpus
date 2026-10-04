from words import get_text, words
def fonk1(b9):
    if not b9:
        return None
    b1 = htable(4011)
    for doc_id, file_name in enumerate(b9):
        b2 = get_text(file_name)
        b3 = words(b2)
        for word in b3:
            b4 = htable_get(b1, word)
            if b4 is None:
                b4 = set()
            b4.add(doc_id)
            htable_put(b1, word, b4)
    return b1
def fonk2(b9, b10, terms):
    if not b9 or not b10 or not terms:
        return None
    b5 = []
    for term in terms:
        b6 = htable_get(b10, term)
        if b6:
            b5.append(b6)
        else:
            return None
    if b5:
        b7 = set.intersection(*b5)
        b8 = [b9[doc_id] for doc_id in b7]
        return b8 if b8 else None
    return None
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