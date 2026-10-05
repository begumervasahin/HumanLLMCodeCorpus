import zipfile
def fonk1(b6, b7):
    try:
        b1 = zipfile.ZipFile(b6)
    except zipfile.BadZipfile:
        print("ERROR: Invalid ZIP file")
        return
    with open(b7, 'r') as f:
        b2 = f.readlines()
        for b3 in b2:
            b3 = b3.strip()
            try:
                b1.extractall(b4 = b3.encode())
                print('Password cracked with: ', b3)
                return
            except Exception:
                pass
        print('Password not found')
if b5 = = "__main__":
    b6 = 'test_zip.zip'
    b7 = 'english.txt'
    fonk1(b6, b7)