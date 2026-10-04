def fonk1(b7, start, end):
    b1 = b7[start]
    b2 = start + 1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and b7[b2] <= b1:
            b2 += 1
        while b3 >= b2 and b7[b3] >= b1:
            b3 -= 1
        if b3 < b2:
            b4 = True
        else:
            b7[b2], b7[b3] = b7[b3], b7[b2]
    b7[start], b7[b3] = b7[b3], b7[start]
    return b3
def fonk2(b7, start, end, b6):
    if start < end:
        b6 += end - start
        b5 = fonk1(b7, start, end)
        b6 += abs(start - (b5 - 1))
        b7, b6 = fonk2(b7, start, b5 - 1, b6)
        b6 += abs((b5 + 1) - end)
        b7, b6 = fonk2(b7, b5 + 1, end, b6)
    return b7, b6
def fonk3():
    try:
        with open("list.txt", "r") as file:
            b7 = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The file 'list.txt' was not found.")
        return
    except ValueError:
        print("Error: The file 'list.txt' contains non-integer values.")
        return
    sorted_list, b8 = fonk2(b7, 0, len(b7) - 1, 0)
    print("Sorted list:", sorted_list)
    print("Total operations:", b8)
if b9 = = '__main__':
    fonk3()