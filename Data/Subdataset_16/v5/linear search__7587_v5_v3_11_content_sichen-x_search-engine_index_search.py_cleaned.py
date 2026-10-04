from collections import defaultdict
from words import get_text, words
def fonk1(b6):
    if not b6:
        return None
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(b6):
        b2 = get_text(file_path)
        b3 = words(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk2(b6, b1, terms):
    if not (b6 and b1 and terms):
        return None
    b4 = [b1.get(term) for term in terms]
    if any(term_set is None for term_set in b4):
        return None
    b5 = set.intersection(*b4)
    return [b6[doc_id] for doc_id in b5]
def fonk3():
    b6 = ["file1.txt", "file2.txt", "file3.txt"]
    b1 = fonk1(b6)
    b7 = ["term1", "term2"]
    b8 = fonk2(b6, b1, b7)
    print("Matching b6:", b8)
if b9 = = "__main__":
    fonk3()