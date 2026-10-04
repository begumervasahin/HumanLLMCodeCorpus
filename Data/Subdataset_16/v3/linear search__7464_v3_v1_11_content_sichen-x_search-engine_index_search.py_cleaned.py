from collections import defaultdict
from words import get_text, words
def fonk1(b7):
    if not b7:
        return None
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(b7):
        b2 = get_text(file_path)
        b3 = words(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk2(b7, b1, terms):
    if not (b7 and b1 and terms):
        return None
    b4 = [b1.get(term) for term in terms if term in b1]
    if not b4 or len(b4) != len(terms):
        return None
    b5 = set.intersection(*b4)
    return [b7[doc_id] for doc_id in b5]
if b6 = = "__main__":
    b7 = ["file1.txt", "file2.txt", "file3.txt"]
    b1 = fonk1(b7)
    b8 = ["term1", "term2"]
    b9 = fonk2(b7, b1, b8)
    print("Matching b7:", b9)