import zipfile
def fonk1():
    try:
        b1 = zipfile.ZipFile('test_zip.zip')
    except zipfile.BadZipfile:
        print("ERROR")
        quit()
    b2 = None
    with open('english.txt','r') as f:
        b3 = f.readlines()
        for x in b3:
            b2 = x.split('\n')[0]
            try:
                print(b2)
                b4 = str.encode((b2))
                b1.extractall(b5 = b4)
                print('Password cracked with : ',b2)
                quit()
            except Exception:
                pass
        print('Password not found')