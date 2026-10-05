def fonk1(List):
    return ''.join(List)
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
    if fonk4(b2, b1) == False:
        return True
    return False
def fonk6(b2):
    if b2 = = 1:
        return 1
    return b2 * fonk6(b2 - 1)
def fonk7(b2, b9):
    if b2 = = 0:
        return 1
    return (b9 ** b2) / fonk6(b2) + fonk7(b2 - 1, b9)
def fonk8(char_list, b2):
    if b2 = = 0:
        return
    b3 = b2
    b2 = len(set(char_list))
    fonk9(char_list, "", b2, b3)
def fonk9(char_list, b10, b2, b3):
    if b3 = = 0:
        print(b10)
        return
    for b1 in range(b2):
        b4 = b10 + char_list[b1]
        fonk9(char_list, b4, b2, b3 - 1)
def fonk10(char_list, b2):
    if b2 = = 0:
        return
    fonk11(char_list, "", b2)
def fonk11(char_list, b10, b2):
    if b2 = = 0:
        print(b10)
        return
    for b1, char in enumerate(char_list):
        b5 = b10 + char
        fonk11(char_list[:b1] + char_list[b1+1:], b5, b2-1)
def fonk12(b2):
    b6 = [""] * 2 * b2
    b7 = []
    if b2 > 0:
        fonk13(b6, 0, b2, 0, 0, b7)
    return b7
def fonk13(b6, pos, b2, open, b8, b7):
    if b8 = = b2:
        b9 = "".join(b6)
        b7.append(b9)
        return
    else:
        if open > b8:
            b6[pos] = ")"
            fonk13(b6, pos + 1, b2, open, b8 + 1, b7)
        if open < b2:
            b6[pos] = "("
            fonk13(b6, pos + 1, b2, open + 1, b8, b7)
def fonk14(b2, b3):
    if b3 = = 0 and b2 == 0:
        return None
    if b2 < 0 or b3 < 0:
        return None
    fonk15(b2, b3, "")
def fonk15(b2, b3, b10 = ''):
    if b2 = = 0 and b3 == 0:
        print(b10)
        return
    elif b2 = = 0:
        fonk15(b2, b3 - 1, b10 + 'u')
        return
    elif b3 = = 0:
        fonk15(b2 - 1, b3, b10 + 'r')
        return
    fonk15(b2, b3 - 1, b10 + 'u')
    fonk15(b2 - 1, b3, b10 + 'r')
def fonk16(image, start):
    """This function changes every "." which is right after the start point or to another "." in one of four
    directions(up down left or right) characters to "*" The main recursive function starting at point (b9, y) changes any "." when located in above valid places to "*" """
    b11 = len(image)
    b12 = len(image[0])
    if image[b9][y] != empty_char:
        return
    image[b9][y] = full_char
    floodFill_rec(image, b9 - 1, y, empty_char, full_char)
    floodFill_rec(image, b9, y - 1, empty_char, full_char)
    floodFill_rec(image, b9 + 1, y, empty_char, full_char)
    floodFill_rec(image, b9, y + 1, empty_char, full_char)
