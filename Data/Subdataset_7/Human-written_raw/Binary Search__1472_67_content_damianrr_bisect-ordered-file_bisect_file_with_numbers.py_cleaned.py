import os
def fonk1(f, search):
    b1 = os.fstat(f.fileno()).st_size
    a1 = 0
    b2 = int(search)
    while b1 - a1 > 1:
        b3 = int((b1 + a1) / 2)
        f.seek(b3)
        b4 = f.tell()
        while f.read(1) != '\n':
            pass
        b5 = f.readline()
        if not b5:
            f.seek(b4)
            f.seek(-1, 1)
            while f.read(1) != '\n':
                f.seek(-2, 1)
            b5 = f.readline()
        b6 = int(b5)
        if b2 < b6:
            b1 = b3
            continue
        if b2 > b6:
            a1 = b3
            continue
        return {"result":b5.replace("\n", ""), "position":f.tell()}
    return False
if b7 = = "__main__":
    import doctest
    doctest.testmod()