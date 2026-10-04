from collections import defaultdict
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(text):
    return text.split()
def fonk3(b6):
    if not b6:
        return None
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(b6):
        b2 = fonk2(fonk1(file_path))
        for word in b2:
            b1[word].add(doc_id)
    return b1
def fonk4(b6, b1, terms):
    if not (b6 and b1 and terms):
        return None
    b3 = [b1.get(term) for term in terms]
    if any(term_set is None for term_set in b3):
        return None
    b4 = set.intersection(*b3)
    return [b6[doc_id] for doc_id in b4]
if b5 = = "__main__":
    b6 = ["file1.txt", "file2.txt", "file3.txt"]
    b1 = fonk3(b6)
    b7 = ["term1", "term2"]
    b8 = fonk4(b6, b1, b7)
    print("Matching b6:", b8)