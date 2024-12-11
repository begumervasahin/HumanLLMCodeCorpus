
def fonk1(lst):
    return ''.join(lst)
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
    b1 = int(b2**0.5)
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
def fonk8(char_list, b2):
    if b2 = = 0:
        return
    b3 = b2
    b2 = len(set(char_list))
    fonk9(char_list, "", b2, b3)
def fonk9(char_list, b11, b3, b4):
    if b4 = = 0:
        print(b11)
        return
    for b1 in range(b3):
        b5 = b11 + char_list[b1]
        fonk9(char_list, b5, b3, b4 - 1)
def fonk10(char_list, b2):
    if b2 = = 0:
        return
    fonk11(char_list, "", b2)
def fonk11(char_list, b11, b2):
    if b2 = = 0:
        print(b11)
        return
    for b1, char in enumerate(char_list):
        b5 = b11 + char
        fonk11(char_list[:b1] + char_list[b1+1:], b5, b2-1)
def fonk12(b2):
    b6 = [""] * 2 * b2
    b7 = []
    if b2 > 0:
        fonk13(b6, 0, b2, 0, 0, b7)
    return b7
def fonk13(b6, pos, b2, open_count, b8, b7):
    if b8 = = b2:
        b9 = "".join(b6)
        b7.append(b9)
        return
    else:
        if open_count > b8:
            b6[pos] = ")"
            fonk13(b6, pos + 1, b2, open_count, b8 + 1, b7)
        if open_count < b2:
            b6[pos] = "("
            fonk13(b6, pos + 1, b2, open_count + 1, b8, b7)
def fonk14(b2, b10):
    if b10 = = 0 and b2 == 0:
        return None
    if b2 < 0 or b10 < 0:
        return None
    fonk15(b2, b10, "")
def fonk15(b2, b10, b11 = ''):
    if b2 = = 0 and b10 == 0:
        print(b11)
        return
    elif b2 = = 0:
        fonk15(b2, b10 - 1, b11 + 'u')
        return
    elif b10 = = 0:
        fonk15(b2 - 1, b10, b11 + 'r')
        return
    fonk15(b2, b10 - 1, b11 + 'u')
    fonk15(b2 - 1, b10, b11 + 'r')
def fonk16(image, start):
    x, b12 = start
    fonk17(image, x, b12, '.', '*')
def fonk17(image, x, b12, empty_char, fill_char):
    b13 = len(image)
    b14 = len(image[0])
    if image[x][b12] != empty_char:
        return
    image[x][b12] = fill_char
    fonk17(image, x - 1, b12, empty_char, fill_char)
    fonk17(image, x, b12 - 1, empty_char, fill_char)
    fonk17(image, x + 1, b12, empty_char, fill_char)
    fonk17(image, x, b12 + 1, empty_char, fill_char)
