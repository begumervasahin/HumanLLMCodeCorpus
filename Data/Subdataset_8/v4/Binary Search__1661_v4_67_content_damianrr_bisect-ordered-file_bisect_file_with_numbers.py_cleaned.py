import os
def bisect_big_file_looking_for_number(file_obj, search_number):
    file_size = os.fstat(file_obj.fileno()).st_size
    low = 0
    high = file_size
    search_number = int(search_number)
    while high - low > 1:
        middle = (high + low)
        file_obj.seek(middle)
        last_pos = file_obj.tell()
        while file_obj.read(1) != '\n':
            pass
        line = file_obj.readline()
        if not line:
            file_obj.seek(last_pos)
            file_obj.seek(-1, 1)
            while file_obj.read(1) != '\n':
                file_obj.seek(-2, 1)
            line = file_obj.readline()
        number_in_line = int(line)
        if search_number < number_in_line:
            high = middle
        elif search_number > number_in_line:
            low = middle
        else:
            return {"result": line.replace("\n", ""), "position": file_obj.tell()}
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()