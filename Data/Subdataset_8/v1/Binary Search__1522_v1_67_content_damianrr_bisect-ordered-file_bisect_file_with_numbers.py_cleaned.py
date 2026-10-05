import os
def bisect_big_file_looking_for_number(f, search):
    high = os.fstat(f.fileno()).st_size
    low = 0
    number = int(search)
    while high - low > 1:
        middle = int((high + low) / 2)
        f.seek(middle)
        last_pos = f.tell()
        while f.read(1) != '\n':
            pass
        line = f.readline()
        if not line:
            f.seek(last_pos)
            f.seek(-1, 1)
            while f.read(1) != '\n':
                f.seek(-2, 1)
            line = f.readline()
        number_in_line = int(line)
        if number < number_in_line:
            high = middle
            continue
        if number > number_in_line:
            low = middle
            continue
        return {"result": line.replace("\n", ""), "position": f.tell()}
    return False
if __name__ == "__main__":
    filename = 'test.log'
    number_to_search = int(input("Enter the number you want to search for: "))
    with open(filename, 'r') as file:
        result = bisect_big_file_looking_for_number(file, number_to_search)
    if result:
        print("Number found:", result)
    else:
        print("Number not found.")