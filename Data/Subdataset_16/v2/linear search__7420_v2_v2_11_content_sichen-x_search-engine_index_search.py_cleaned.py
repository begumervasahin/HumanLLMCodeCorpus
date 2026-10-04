from collections import defaultdict
def fonk1(file_path):
    with open(file_path, 'r', b1 = 'utf-8') as file:
        return file.read()
def fonk2(text):
    return text.lower().split()
def fonk3(b8):
    if not b8:
        return None
    b2 = defaultdict(set)
    for i, file_path in enumerate(b8):
        b3 = fonk1(file_path)
        b4 = fonk2(b3)
        for word in b4:
            b2[word].add(i)
    return b2
def fonk4(b8, b2, terms):
    if not (b8 and b2 and terms):
        return None
    b5 = [b2.get(term) for term in terms if b2.get(term)]
    if len(b5) != len(terms):
        return None
    b6 = set.intersection(*b5)
    return [b8[id] for id in b6] if b6 else None
if b7 = = "__main__":
    b8 = ["file1.txt", "file2.txt", "file3.txt"]
    b2 = fonk3(b8)
    b9 = ["term1", "term2"]
    b10 = fonk4(b8, b2, b9)
    print("Matching b8:", b10)