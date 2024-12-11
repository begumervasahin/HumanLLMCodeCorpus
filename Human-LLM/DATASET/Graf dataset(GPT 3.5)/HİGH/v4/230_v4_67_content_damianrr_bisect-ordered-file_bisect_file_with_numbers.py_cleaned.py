import os
def fonk1(file_obj, b3):
    b1 = os.fstat(file_obj.fileno()).st_size
    a1 = 0
    b2 = b1
    b3 = int(b3)
    while b2 - a1 > 1:
        b4 = (b2 + a1)
        file_obj.seek(b4)
        b5 = file_obj.tell()
        while file_obj.read(1) != '\n':
            pass
        b6 = file_obj.readline()
        if not b6:
            file_obj.seek(b5)
            file_obj.seek(-1, 1)
            while file_obj.read(1) != '\n':
                file_obj.seek(-2, 1)
            b6 = file_obj.readline()
        b7 = int(b6)
        if b3 < b7:
            b2 = b4
        elif b3 > b7:
            a1 = b4
        else:
            return {"result": b6.replace("\n", ""), "position": file_obj.tell()}
    return False
if b8 = = "__main__":
    import doctest
    doctest.testmod()