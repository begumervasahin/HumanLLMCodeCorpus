import os
def fonk1(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None
def fonk2(text):
    return text.split()
def fonk3(b4, b5):
    if not b4 or not b5:
        return None
    b1 = []
    for file_path in b4:
        b2 = fonk1(file_path)
        if b2:
            b3 = fonk2(b2)
            if all(term in b3 for term in b5):
                b1.append(file_path)
    return b1
def fonk4():
    b4 = ["file1.txt", "file2.txt", "file3.txt"]
    b5 = ["term1", "term2", "term3"]
    b6 = fonk3(b4, b5)
    if b6:
        print("Files containing all search terms:")
        for file_path in b6:
            print(file_path)
    else:
        print("No b4 found containing all search terms.")
if b7 = = "__main__":
    fonk4()