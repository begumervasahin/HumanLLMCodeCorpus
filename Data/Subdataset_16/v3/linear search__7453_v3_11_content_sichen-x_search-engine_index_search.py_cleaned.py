from collections import defaultdict
from words import get_text, words
def fonk1(files):
    if not files:
        return None
    b1 = defaultdict(set)
    for doc_id, file in enumerate(files):
        b2 = get_text(file)
        b3 = words(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk2(files, b1, terms):
    if not files or not b1 or not terms:
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
        return [files[doc_id] for doc_id in b6]
    return None
