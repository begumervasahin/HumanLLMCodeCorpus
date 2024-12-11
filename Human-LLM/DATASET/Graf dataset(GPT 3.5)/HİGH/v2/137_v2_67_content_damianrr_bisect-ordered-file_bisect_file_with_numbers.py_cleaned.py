import os
def fonk1(file_obj, search_number):
    b1 = os.fstat(file_obj.fileno()).st_size
    a1 = 0
    b2 = b1
    b3 = int(search_number)
    while b2 - a1 > 1:
        b4 = int((b2 + a1) / 2)
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
            return {"b11": b6.replace("\n", ""), "position": file_obj.tell()}
    return False
if b8 = = "__main__":
    b9 = 'test.log'
    b10 = int(input("Enter the number you want to search for: "))
    with open(b9, 'r') as file:
        b11 = fonk1(file, b10)
    if b11:
        print("Number found:", b11)
    else:
        print("Number not found.")