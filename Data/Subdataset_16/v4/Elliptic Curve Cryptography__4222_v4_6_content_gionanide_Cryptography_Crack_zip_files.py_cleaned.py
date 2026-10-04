import zipfile
def fonk1(b5, b6):
    try:
        b1 = zipfile.ZipFile(b5)
    except zipfile.BadZipFile:
        print("ERROR: Not a valid zip file")
        return
    with open(b6, 'r') as file:
        b2 = file.readlines()
    for b3 in b2:
        b3 = b3.strip()
        try:
            print(f"Trying b3: {b3}")
            b1.extractall(b4 = b3.encode())
            print(f"Password cracked with: {b3}")
            return
        except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
            continue
    print("Password not found")
def fonk2():
    b5 = 'test_zip.zip'
    b6 = 'english.txt'
    fonk1(b5, b6)
if b7 = = "__main__":
    fonk2()