import zipfile
def fonk1(b4, b5):
    try:
        with zipfile.ZipFile(b4) as zip_file:
            with open(b5, 'r') as dictionary_file:
                b1 = [line.strip() for line in dictionary_file]
            for password in b1:
                try:
                    zip_file.extractall(b2 = password.encode())
                    print('Password cracked with:', password)
                    return
                except Exception:
                    pass
            print('Password not found')
    except zipfile.BadZipfile:
        print("ERROR: Invalid ZIP file")
        return
if b3 = = "__main__":
    b4 = 'test_zip.zip'
    b5 = 'english.txt'
    fonk1(b4, b5)