def fonk1(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError:
        return None
def fonk2(text):
    return text.split()
def fonk3(b5, terms):
    if not b5 or not terms:
        return None
    b1 = []
    for file_path in b5:
        b2 = fonk1(file_path)
        if b2:
            b3 = fonk2(b2)
            if all(term in b3 for term in terms):
                b1.append(file_path)
    return b1
if b4 = = "__main__":
    b5 = ["file1.txt", "file2.txt", "file3.txt"]
    b6 = ["term1", "term2", "term3"]
    b7 = fonk3(b5, b6)
    print("Files containing all search terms:")
    if b7:
        for file in b7:
            print(file)
    else:
        print("No b5 contain all search terms.")