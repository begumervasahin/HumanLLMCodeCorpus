from words import get_text, words
def fonk1(b8):
    if not b8:
        return None
    b1 = htable(4011)
    for doc_id, file_name in enumerate(b8):
        b2 = get_text(file_name)
        b3 = words(b2)
        for word in b3:
            htable_put(b1, word, {doc_id})
    return b1
def fonk2(b8, b9, terms):
    if not b8 or not b9 or not terms:
        return None
    b4 = []
    for term in terms:
        b5 = htable_get(b9, term)
        if b5:
            b4.append(b5)
        else:
            return None
    if b4:
        b6 = set.intersection(*b4)
        b7 = [b8[doc_id] for doc_id in b6]
        return b7 if b7 else None
    return None
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