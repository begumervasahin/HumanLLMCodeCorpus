import os
def fonk1(file, target):
    b6, b1 = 0, os.fstat(file.fileno()).st_size
    b2 = int(target)
    while b1 - b6 > 1:
        b3 = (b1 + b6)
        file.seek(b3)
        file.readline()
        b4 = file.readline()
        if not b4:
            b1 = b3
            continue
        b5 = int(b4.strip())
        if b2 < b5:
            b1 = b3
        elif b2 > b5:
            b6 = file.tell()
        else:
            return {"b8": b4.strip(), "position": file.tell()}
    return False
if b7 = = "__main__":
    import doctest
    doctest.testmod()
    with open('test.log', 'r') as file:
        a1 = 59953
        b8 = fonk1(file, a1)
        if b8:
            print(f"Number {a1} found at position {b8['position']}")
        else:
            print(f"Number {a1} not found.")