def fonk1(file):
    pass
def fonk2(text):
    pass
def fonk3(files, terms):
    if not files or not terms:
        return None
    b1 = []
    for file in files:
        b2 = fonk1(file)
        if b2:
            b3 = fonk2(b2)
            if all(term in b3 for term in terms):
                b1.append(file)
    return b1
if b4 = = "__main__":
    b5 = ["file1.txt", "file2.txt", "file3.txt"]
    b6 = ["term1", "term2", "term3"]
    b7 = fonk3(b5, b6)
    print("Files containing all search terms:")
    for file in b7:
        print(file)