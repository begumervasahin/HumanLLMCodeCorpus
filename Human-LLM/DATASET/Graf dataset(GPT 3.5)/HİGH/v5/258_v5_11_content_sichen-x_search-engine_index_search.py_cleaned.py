from collections import defaultdict
from words import get_text, words
def fonk1(files):
    if not files:
        return None
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        b2 = get_text(file_path)
        b3 = words(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk2(files, b1, terms):
    if not files or not b1 or not terms:
        return None
    b4 = [b1.get(term) for term in terms]
    if not all(b4):
        return None
    b5 = set.intersection(*b4)
    b6 = [files[doc_id] for doc_id in b5]
    return b6