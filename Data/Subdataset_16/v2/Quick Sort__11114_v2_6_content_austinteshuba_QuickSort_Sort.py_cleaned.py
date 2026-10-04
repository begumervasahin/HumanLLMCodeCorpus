def fonk1(b6, start, end):
    b1 = b6[start]
    b2 = start + 1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and b6[b2] <= b1:
            b2 += 1
        while b3 >= b2 and b6[b3] >= b1:
            b3 -= 1
        if b3 < b2:
            b4 = True
        else:
            b6[b2], b6[b3] = b6[b3], b6[b2]
    b6[start], b6[b3] = b6[b3], b6[start]
    return b3
a1 = 0
def fonk2(b6, start, end):
    global a1
    if start < end:
        a1 += end - start
        b5 = fonk1(b6, start, end)
        a1 += abs(start - (b5 - 1))
        fonk2(b6, start, b5 - 1)
        a1 += abs((b5 + 1) - end)
        fonk2(b6, b5 + 1, end)
    return b6
def fonk3():
    try:
        with open("list.txt", "r") as file:
            b6 = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The file 'list.txt' was not found.")
        return
    except ValueError:
        print("Error: The file 'list.txt' contains non-integer values.")
        return
    b7 = fonk2(b6, 0, len(b6) - 1)
    print("Sorted list:", b7)
    print("Total operations:", a1)
if b8 = = '__main__':
    fonk3()