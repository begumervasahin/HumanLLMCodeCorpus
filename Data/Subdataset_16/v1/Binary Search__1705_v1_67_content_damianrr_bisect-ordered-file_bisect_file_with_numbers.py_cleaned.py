import os
def fonk1(f, search):
    b1 = os.fstat(f.fileno()).st_size
    a1 = 0
    b2 = int(search)
    while b1 - a1 > 1:
        b3 = (b1 + a1)
        f.seek(b3)
        b4 = f.tell()
        while f.read(1) != '\n' and f.tell() < b1:
            pass
        b5 = f.readline()
        if not b5:
            f.seek(b4)
            f.seek(-1, os.SEEK_CUR)
            while f.read(1) != '\n' and f.tell() > 0:
                f.seek(-2, os.SEEK_CUR)
            b5 = f.readline()
        if not b5:
            return False
        b6 = int(b5.strip())
        if b2 < b6:
            b1 = b3
        elif b2 > b6:
            a1 = b3
        else:
            return {"b8": b5.strip(), "position": f.tell()}
    return False
if b7 = = "__main__":
    import doctest
    doctest.testmod()
    with open('test.log', 'r') as f:
        a2 = 59953
        b8 = fonk1(f, a2)
        if b8:
            print(f"Number {a2} found at position {b8['position']}")
        else:
            print(f"Number {a2} not found.")