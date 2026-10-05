def fonk1(char_list):
    return ''.join(char_list)
def fonk2(b2):
    if b2 >= 1:
        fonk2(b2 - 1)
        print(str(b2))
    else:
        return
def fonk3(b2):
    if b2 >= 1:
        print(str(b2))
        fonk3(b2 - 1)
def fonk4(b2, b1):
    if b1 = = 1 or b1 == 0:
        return False
    elif b2 % b1 = = 0:
        return True
    return fonk4(b2, b1 - 1)
def fonk5(b2):
    if b2 < 2:
        return False
    b1 = int(b2 ** 0.5)
    if not fonk4(b2, b1):
        return True
    return False
def fonk6(b2):
    if b2 = = 1:
        return 1
    return b2 * fonk6(b2 - 1)
def fonk7(b2, x):
    if b2 = = 0:
        return 1
    return (x ** b2) / fonk6(b2) + fonk7(b2 - 1, x)
def fonk8(hanoi, b2, src, dest, temp):
    if b2 < 1:
        return
    elif b2 = = 1:
        hanoi.move(src, dest)
        return
    fonk8(hanoi, b2 - 1, src, temp, dest)
    hanoi.move(src, dest)
    fonk8(hanoi, b2 - 1, temp, dest, src)
def fonk9(char_list, b2):
    if b2 = = 0:
        return
    b3 = b2
    b2 = len(set(char_list))
    fonk10(char_list, "", b2, b3)
def fonk10(char_list, b9, b2, b3):
    if b3 = = 0:
        print(b9)
        return
    for b1 in range(b2):
        b4 = b9 + char_list[b1]
        fonk10(char_list, b4, b2, b3 - 1)
def fonk11(char_list, b2):
    if b2 = = 0:
        return
    fonk12(char_list, "", b2)
def fonk12(char_list, b9, b2):
    if b2 = = 0:
        print(b9)
        return
    for b1, char in enumerate(char_list):
        b4 = b9 + char
        fonk12(char_list[:b1] + char_list[b1+1:], b4, b2 - 1)
def fonk13(b2):
    b5 = [""] * 2 * b2
    b6 = []
    if b2 > 0:
        fonk14(b5, 0, b2, 0, 0, b6)
    return b6
def fonk14(b5, pos, b2, open, b7, b6):
    if b7 = = b2:
        b8 = "".join(b5)
        b6.append(b8)
        return
    else:
        if open > b7:
            b5[pos] = ')'
            fonk14(b5, pos + 1, b2, open, b7 + 1, b6)
        if open < b2:
            b5[pos] = '('
            fonk14(b5, pos + 1, b2, open + 1, b7, b6)
def fonk15(b2, b3):
    if b3 = = 0 and b2 == 0:
        return None
    if b2 < 0 or b3 < 0:
        return None
    fonk16(b2, b3, "")
def fonk16(b2, b3, b9 = ''):
    if b2 = = 0 and b3 == 0:
        print(b9)
        return
    elif b2 = = 0:
        fonk16(b2, b3 - 1, b9 + 'u')
        return
    elif b3 = = 0:
        fonk16(b2 - 1, b3, b9 + 'r')
        return
    fonk16(b2, b3 - 1, b9 + 'u')
    fonk16(b2 - 1, b3, b9 + 'r')
def fonk17(image, start):
    x, b10 = start
    fonk18(image, x, b10, '.', '*')
def fonk18(image, x, b10, empty_char, full_char):
    b11 = len(image)
    b12 = len(image[0])
    if image[x][b10] != empty_char:
        return
    image[x][b10] = full_char
    fonk18(image, x - 1, b10, empty_char, full_char)
    fonk18(image, x, b10 - 1, empty_char, full_char)
    fonk18(image, x + 1, b10, empty_char, full_char)
    fonk18(image, x, b10 + 1, empty_char, full_char)