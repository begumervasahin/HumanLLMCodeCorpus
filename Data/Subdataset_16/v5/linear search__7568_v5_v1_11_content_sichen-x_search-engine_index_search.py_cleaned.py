from collections import defaultdict
from words import get_text, words
def fonk1(b8):
    if not b8:
        return None
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(b8):
        b2 = get_text(file_path)
        b3 = words(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk2(b8, b1, terms):
    if not (b8 and b1 and terms):
        return None
    b4 = []
    for term in terms:
        b5 = b1.get(term)
        if b5:
            b4.append(b5)
        else:
            return None
    if b4:
        b6 = set.intersection(*b4)
        return [b8[doc_id] for doc_id in b6]
    else:
        return None
if b7 = = "__main__":
    b8 = ["file1.txt", "file2.txt", "file3.txt"]
    b1 = fonk1(b8)
    b9 = ["term1", "term2"]
    b10 = fonk2(b8, b1, b9)
    print("Matching b8:", b10)