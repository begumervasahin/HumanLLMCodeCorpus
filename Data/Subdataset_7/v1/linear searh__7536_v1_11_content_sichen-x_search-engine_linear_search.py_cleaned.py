
def fonk1(file):
    pass
def fonk2(text):
    pass
def fonk3(b5, terms):
    if b5 is None or terms is None or len(b5) == 0 or len(terms) == 0:
        return None
    b1 = []
    for file in b5:
        b2 = fonk1(file)
        if b2 is not None:
            b3 = all(term in fonk2(b2) for term in terms)
            if b3:
                b1.append(file)
    return b1
if b4 = = "__main__":
    b5 = ["file1.txt", "file2.txt", "file3.txt"]
    b6 = ["term1", "term2", "term3"]
    b7 = fonk3(b5, b6)
    print("Files containing all search terms:")
    for file in b7:
        print(file)