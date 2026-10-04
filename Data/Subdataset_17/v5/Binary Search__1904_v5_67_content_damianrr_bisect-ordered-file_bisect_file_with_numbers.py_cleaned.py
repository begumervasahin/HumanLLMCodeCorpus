import os
def bisect_big_file_looking_for_number(f, search):
    file_size = os.fstat(f.fileno()).st_size
    low, high = 0, file_size
    target_number = int(search)
    while high - low > 1:
        middle = (high + low)
        f.seek(middle)
        while f.read(1) != '\n':
            if f.tell() >= high:
                break
        line = f.readline()
        if not line.strip():
            f.seek(middle)
            while middle > 0 and f.read(1) != '\n':
                f.seek(middle - 2, os.SEEK_SET)
                middle -= 1
            line = f.readline()
        if not line.strip():
            break
        number_in_line = int(line.strip())
        if target_number < number_in_line:
            high = middle
        elif target_number > number_in_line:
            low = f.tell()
        else:
            return {"result": line.strip(), "position": f.tell()}
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()