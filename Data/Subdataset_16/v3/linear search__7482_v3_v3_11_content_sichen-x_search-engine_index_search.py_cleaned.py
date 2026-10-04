from collections import defaultdict
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(text):
    return text.split()
def fonk3(b6):
    b1 = defaultdict(set)
    for doc_id, file_path in enumerate(b6):
        b2 = fonk1(file_path)
        b3 = fonk2(b2)
        for word in b3:
            b1[word].add(doc_id)
    return b1
def fonk4(b6, b1, terms):
    if not terms:
        return []
    b4 = [b1.get(term) for term in terms if b1.get(term)]
    if not b4:
        return []
    b5 = set.intersection(*b4)
    return [b6[doc_id] for doc_id in b5]
def fonk5():
    b6 = ["file1.txt", "file2.txt", "file3.txt"]
    b1 = fonk3(b6)
    b7 = ["term1", "term2"]
    b8 = fonk4(b6, b1, b7)
    print("Matching b6:", b8)
if b9 = = "__main__":
    fonk5()