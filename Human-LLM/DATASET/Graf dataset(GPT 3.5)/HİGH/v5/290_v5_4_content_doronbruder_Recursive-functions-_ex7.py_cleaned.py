def fonk1(char_list):
    return ''.join(char_list)
def fonk2(b2):
    if b2 < 1:
        return
    for b1 in range(1, b2 + 1):
        print(b1)
def fonk3(b2):
    if b2 < 1:
        return
    for b1 in range(b2, 0, -1):
        print(b1)
def fonk4(b2, b1):
    if b1 <= 1:
        return False
    if b2 % b1 = = 0:
        return True
    return fonk4(b2, b1 - 1)
def fonk5(b2):
    if b2 < 2:
        return False
    return not fonk4(b2, int(b2 ** 0.5))
def fonk6(b2):
    if b2 = = 0:
        return 1
    return b2 * fonk6(b2 - 1)
def fonk7(b2, x):
    return (x ** b2) / fonk6(b2) + fonk7(b2 - 1, x) if b2 > 0 else 1
def fonk8(hanoi, b2, src, dest, temp):
    if b2 < 1:
        return
    if b2 = = 1:
        hanoi.move(src, dest)
        return
    fonk8(hanoi, b2 - 1, src, temp, dest)
    hanoi.move(src, dest)
    fonk8(hanoi, b2 - 1, temp, dest, src)
def fonk9(char_list, b2):
    if b2 < 1:
        return
    fonk10(char_list, "", b2)
def fonk10(char_list, b7, b3):
    if b3 = = 0:
        print(b7)
        return
    for char in char_list:
        b4 = b7 + char
        fonk10(char_list, b4, b3 - 1)
def fonk11(char_list, b2):
    if b2 < 1:
        return
    fonk12(char_list, "", b2)
def fonk12(char_list, b7, b2):
    if b2 = = 0:
        print(b7)
        return
    for b1, char in enumerate(char_list):
        b4 = b7 + char
        fonk12(char_list[:b1] + char_list[b1+1:], b4, b2 - 1)
def fonk13(b2):
    b5 = []
    if b2 > 0:
        fonk14([""] * 2 * b2, 0, b2, 0, 0, b5)
    return b5
def fonk14(str_lst, pos, b2, open_count, b6, b5):
    if b6 = = b2:
        b5.append("".join(str_lst))
        return
    if open_count > b6:
        str_lst[pos] = ')'
        fonk14(str_lst, pos + 1, b2, open_count, b6 + 1, b5)
    if open_count < b2:
        str_lst[pos] = '('
        fonk14(str_lst, pos + 1, b2, open_count + 1, b6, b5)
def fonk15(b2, b3):
    if b2 < 0 or b3 < 0:
        return None
    fonk16(b2, b3, "")
def fonk16(b2, b3, b7 = ''):
    if b2 = = 0 and b3 == 0:
        print(b7)
        return
    if b2 > 0:
        fonk16(b2 - 1, b3, b7 + 'r')
    if b3 > 0:
        fonk16(b2, b3 - 1, b7 + 'u')
def fonk17(image, start):
    x, b8 = start
    fonk18(image, x, b8, '.', '*')
def fonk18(image, x, b8, empty_char, full_char):
    if x < 0 or b8 < 0 or x >= len(image) or b8 >= len(image[0]) or image[x][b8] != empty_char:
        return
    image[x][b8] = full_char
    fonk18(image, x - 1, b8, empty_char, full_char)
    fonk18(image, x, b8 - 1, empty_char, full_char)
    fonk18(image, x + 1, b8, empty_char, full_char)
    fonk18(image, x, b8 + 1, empty_char, full_char)