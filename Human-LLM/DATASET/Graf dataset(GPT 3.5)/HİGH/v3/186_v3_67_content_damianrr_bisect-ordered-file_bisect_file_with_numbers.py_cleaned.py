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
            return {"b10": b6.replace("\n", ""), "position": file_obj.tell()}
    return False
def fonk2():
    b8 = 'test.log'
    b9 = int(input("Enter the number you want to search for: "))
    with open(b8, 'r') as file:
        b10 = fonk1(file, b9)
    if b10:
        print("Number found:", b10["b10"])
        print("Position in file:", b10["position"])
    else:
        print("Number not found.")
if b11 = = "__main__":
    fonk2()