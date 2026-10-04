import zipfile
def fonk1(b4, b5):
    try:
        with zipfile.ZipFile(b4) as myzip:
            with open(b5, 'r') as f:
                b1 = f.readlines()
                for b2 in b1:
                    b2 = b2.strip()
                    try:
                        print(f"Trying b2: {b2}")
                        myzip.extractall(b3 = b2.encode())
                        print(f"Password cracked with: {b2}")
                        return
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                        continue
                print("Password not found")
    except zipfile.BadZipFile:
        print("ERROR: Not a valid zip file")
        return
def fonk2():
    b4 = 'test_zip.zip'
    b5 = 'english.txt'
    fonk1(b4, b5)
if b6 = = "__main__":
    fonk2()