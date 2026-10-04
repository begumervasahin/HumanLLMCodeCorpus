import os
def bisect_big_file_looking_for_number(f, search):
    high = os.fstat(f.fileno()).st_size
    low = 0
    target_number = int(search)
    while high - low > 1:
        middle = (high + low)
        f.seek(middle)
        while f.read(1) != '\n':
            if f.tell() == high:
                break
        line = f.readline()
        if not line:
            f.seek(-1, 1)
            while f.read(1) != '\n' and f.tell() > 0:
                f.seek(-2, 1)
            line = f.readline()
        if not line.strip():
            break
        number_in_line = int(line.strip())
        if target_number < number_in_line:
            high = middle
        elif target_number > number_in_line:
            low = middle
        else:
            return {"result": line.strip(), "position": f.tell()}
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()