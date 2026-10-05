
def fonk1(lst):
    return ''.join(lst)
def fonk2(b3):
    if b3 >= 1:
        fonk2(b3 - 1)
        print(str(b3))
    else:
        return
def fonk3(b3):
    if b3 >= 1:
        print(str(b3))
        fonk3(b3 - 1)
def fonk4(b3, b1):
    if b1 <= 1:
        return False
    elif b3 % b1 = = 0:
        return True
    return fonk4(b3, b1 - 1)
def fonk5(b3):
    if b3 < 2:
        return False
    b2 = int(b3 ** 0.5)
    return not fonk4(b3, b2)
def fonk6(b3):
    if b3 = = 1:
        return 1
    return b3 * fonk6(b3 - 1)
def fonk7(b3, x):
    if b3 = = 0:
        return 1
    return (x ** b3) / fonk6(b3) + fonk7(b3 - 1, x)
def fonk8(char_list, b3):
    if b3 = = 0:
        return
    b4 = b3
    b5 = len(set(char_list))
    fonk9(char_list, "", b5, b3)
def fonk9(char_list, b13, b4, b6):
    if b6 = = 0:
        print(b13)
        return
    for b1 in range(b4):
        b7 = b13 + char_list[b1]
        fonk9(char_list, b7, b4, b6 - 1)
def fonk10(char_list, b3):
    if b3 = = 0:
        return
    fonk11(char_list, "", b3)
def fonk11(char_list, b13, b3):
    if b3 = = 0:
        print(b13)
        return
    for b1, char in enumerate(char_list):
        b7 = b13 + char
        fonk11(char_list[:b1] + char_list[b1+1:], b7, b3-1)
def fonk12(b3):
    b8 = [""] * 2 * b3
    b9 = []
    if b3 > 0:
        fonk13(b8, 0, b3, 0, 0, b9)
    return b9
def fonk13(b8, pos, b3, open_count, b10, b9):
    if b10 = = b3:
        b11 = "".join(b8)
        b9.append(b11)
        return
    else:
        if open_count > b10:
            b8[pos] = ")"
            fonk13(b8, pos + 1, b3, open_count, b10 + 1, b9)
        if open_count < b3:
            b8[pos] = "("
            fonk13(b8, pos + 1, b3, open_count + 1, b10, b9)
def fonk14(b3, b12):
    if b12 = = 0 and b3 == 0:
        return None
    if b3 < 0 or b12 < 0:
        return None
    fonk15(b3, b12, "")
def fonk15(b3, b12, b13 = ''):
    if b3 = = 0 and b12 == 0:
        print(b13)
        return
    elif b3 = = 0:
        fonk15(b3, b12 - 1, b13 + 'u')
        return
    elif b12 = = 0:
        fonk15(b3 - 1, b12, b13 + 'r')
        return
    fonk15(b3, b12 - 1, b13 + 'u')
    fonk15(b3 - 1, b12, b13 + 'r')
def fonk16(image, start):
    x, b14 = start
    fonk17(image, x, b14, '.', '*')
def fonk17(image, x, b14, empty_char, fill_char):
    b15 = len(image)
    b16 = len(image[0])
    if image[x][b14] != empty_char:
        return
    image[x][b14] = fill_char
    fonk17(image, x - 1, b14, empty_char, fill_char)
    fonk17(image, x, b14 - 1, empty_char, fill_char)
    fonk17(image, x + 1, b14, empty_char, fill_char)
    fonk17(image, x, b14 + 1, empty_char, fill_char)
