import os
def fonk1(f, search):
    b1 = os.fstat(f.fileno()).st_size
    b7, b2 = 0, b1
    b3 = int(search)
    while b2 - b7 > 1:
        b4 = (b2 + b7)
        f.seek(b4)
        while f.read(1) != '\n':
            if f.tell() >= b2:
                break
        b5 = f.readline()
        if not b5.strip():
            f.seek(b4)
            while b4 > 0 and f.read(1) != '\n':
                f.seek(b4 - 2, os.SEEK_SET)
                b4 -= 1
            b5 = f.readline()
        if not b5.strip():
            break
        b6 = int(b5.strip())
        if b3 < b6:
            b2 = b4
        elif b3 > b6:
            b7 = f.tell()
        else:
            return {"result": b5.strip(), "position": f.tell()}
    return False
if b8 = = "__main__":
    import doctest
    doctest.testmod()