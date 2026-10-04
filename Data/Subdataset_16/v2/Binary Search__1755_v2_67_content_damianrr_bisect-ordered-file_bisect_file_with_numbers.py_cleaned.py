import os
def fonk1(file, target):
    b7, b1 = 0, os.fstat(file.fileno()).st_size
    b2 = int(target)
    while b1 - b7 > 1:
        b3 = (b1 + b7)
        file.seek(b3)
        b4 = file.tell()
        while file.read(1) != '\n' and file.tell() < b1:
            pass
        b5 = file.readline()
        if not b5:
            file.seek(b4)
            file.seek(-1, os.SEEK_CUR)
            while file.read(1) != '\n' and file.tell() > 0:
                file.seek(-2, os.SEEK_CUR)
            b5 = file.readline()
        if not b5:
            return False
        b6 = int(b5.strip())
        if b2 < b6:
            b1 = b3
        elif b2 > b6:
            b7 = b3
        else:
            return {"b9": b5.strip(), "position": file.tell()}
    return False
if b8 = = "__main__":
    import doctest
    doctest.testmod()
    with open('test.log', 'r') as file:
        a1 = 59953
        b9 = fonk1(file, a1)
        if b9:
            print(f"Number {a1} found at position {b9['position']}")
        else:
            print(f"Number {a1} not found.")