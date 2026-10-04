import os
def fonk1(f, search):
    b1 = os.fstat(f.fileno()).st_size
    a1 = 0
    b2 = int(search)
    while b1 - a1 > 1:
        b3 = (b1 + a1)
        f.seek(b3)
        while f.read(1) != '\n':
            if f.tell() == b1:
                break
        b4 = f.readline()
        if not b4:
            f.seek(-1, 1)
            while f.read(1) != '\n' and f.tell() > 0:
                f.seek(-2, 1)
            b4 = f.readline()
        if not b4.strip():
            break
        b5 = int(b4.strip())
        if b2 < b5:
            b1 = b3
        elif b2 > b5:
            a1 = b3
        else:
            return {"result": b4.strip(), "position": f.tell()}
    return False
if b6 = = "__main__":
    import doctest
    doctest.testmod()