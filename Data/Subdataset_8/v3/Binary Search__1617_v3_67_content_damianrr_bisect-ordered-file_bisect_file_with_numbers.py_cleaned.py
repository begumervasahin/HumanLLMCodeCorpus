import os
def search_number_in_big_file(file_obj, search_number):
    file_size = os.fstat(file_obj.fileno()).st_size
    low = 0
    high = file_size
    target_number = int(search_number)
    while high - low > 1:
        middle = int((high + low) / 2)
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
        if target_number < number_in_line:
            high = middle
        elif target_number > number_in_line:
            low = middle
        else:
            return {"result": line.replace("\n", ""), "position": file_obj.tell()}
    return False
def main():
    filename = 'test.log'
    number_to_search = int(input("Enter the number you want to search for: "))
    with open(filename, 'r') as file:
        result = search_number_in_big_file(file, number_to_search)
    if result:
        print("Number found:", result["result"])
        print("Position in file:", result["position"])
    else:
        print("Number not found.")
if __name__ == "__main__":
    main()