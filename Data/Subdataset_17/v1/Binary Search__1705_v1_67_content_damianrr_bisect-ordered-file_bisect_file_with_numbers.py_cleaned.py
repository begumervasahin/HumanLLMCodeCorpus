import os
def bisect_big_file_looking_for_number(f, search):
    high = os.fstat(f.fileno()).st_size
    low = 0
    number = int(search)
    while high - low > 1:
        middle = (high + low)
        f.seek(middle)
        last_pos = f.tell()
        while f.read(1) != '\n' and f.tell() < high:
            pass
        line = f.readline()
        if not line:
            f.seek(last_pos)
            f.seek(-1, os.SEEK_CUR)
            while f.read(1) != '\n' and f.tell() > 0:
                f.seek(-2, os.SEEK_CUR)
            line = f.readline()
        if not line:
            return False
        number_in_line = int(line.strip())
        if number < number_in_line:
            high = middle
        elif number > number_in_line:
            low = middle
        else:
            return {"result": line.strip(), "position": f.tell()}
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    with open('test.log', 'r') as f:
        search_value = 59953
        result = bisect_big_file_looking_for_number(f, search_value)
        if result:
            print(f"Number {search_value} found at position {result['position']}")
        else:
            print(f"Number {search_value} not found.")