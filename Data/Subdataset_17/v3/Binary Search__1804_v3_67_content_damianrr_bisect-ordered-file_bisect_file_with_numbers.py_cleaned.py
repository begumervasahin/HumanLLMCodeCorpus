import os
def bisect_big_file_looking_for_number(file, target):
    low, high = 0, os.fstat(file.fileno()).st_size
    target_number = int(target)
    while high - low > 1:
        middle = (high + low)
        file.seek(middle)
        file.readline()
        line = file.readline()
        if not line:
            high = middle
            continue
        current_number = int(line.strip())
        if target_number < current_number:
            high = middle
        elif target_number > current_number:
            low = file.tell()
        else:
            return {"result": line.strip(), "position": file.tell()}
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    with open('test.log', 'r') as file:
        search_value = 59953
        result = bisect_big_file_looking_for_number(file, search_value)
        if result:
            print(f"Number {search_value} found at position {result['position']}")
        else:
            print(f"Number {search_value} not found.")