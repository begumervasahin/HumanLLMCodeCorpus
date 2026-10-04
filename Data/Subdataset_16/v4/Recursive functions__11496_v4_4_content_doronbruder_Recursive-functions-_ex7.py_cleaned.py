def fonk1(lst):
    return ''.join(lst)
def fonk2(b2):
    if b2 >= 1:
        fonk2(b2 - 1)
        print(b2)
def fonk3(b2):
    if b2 >= 1:
        print(b2)
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
    return not fonk4(b2, b1)
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
    b3 = list(set(char_list))
    fonk10(b3, "", len(b3), b2)
def fonk10(char_list, prefix, b2, b4):
    if b4 = = 0:
        print(prefix)
        return
    for b1 in range(b2):
        b5 = prefix + char_list[b1]
        fonk10(char_list, b5, b2, b4 - 1)
def fonk11(char_list, b2):
    if b2 = = 0:
        return
    fonk12(char_list, "", b2)
def fonk12(char_list, prefix, b2):
    if b2 = = 0:
        print(prefix)
        return
    for b1, char in enumerate(char_list):
        b5 = prefix + char
        fonk12(char_list[:b1] + char_list[b1+1:], b5, b2 - 1)
def fonk13(b2):
    b6 = []
    if b2 > 0:
        fonk14([""] * 2 * b2, 0, b2, 0, 0, b6)
    return b6
def fonk14(curr, pos, b2, open_count, b7, b6):
    if b7 = = b2:
        b6.append("".join(curr))
        return
    if open_count > b7:
        curr[pos] = ')'
        fonk14(curr, pos + 1, b2, open_count, b7 + 1, b6)
    if open_count < b2:
        curr[pos] = '('
        fonk14(curr, pos + 1, b2, open_count + 1, b7, b6)
def fonk15(b2, b4):
    if b2 < 0 or b4 < 0:
        return None
    fonk16(b2, b4, "")
def fonk16(b2, b4, prefix):
    if b2 = = 0 and b4 == 0:
        print(prefix)
        return
    if b2 > 0:
        fonk16(b2 - 1, b4, prefix + 'r')
    if b4 > 0:
        fonk16(b2, b4 - 1, prefix + 'u')
def fonk17(image, start):
    x, b8 = start
    fonk18(image, x, b8, '.', '*')
def fonk18(image, x, b8, empty_char, fill_char):
    b9 = len(image)
    b10 = len(image[0])
    if x < 0 or x >= b9 or b8 < 0 or b8 >= b10 or image[x][b8] != empty_char:
        return
    image[x][b8] = fill_char
    fonk18(image, x - 1, b8, empty_char, fill_char)
    fonk18(image, x + 1, b8, empty_char, fill_char)
    fonk18(image, x, b8 - 1, empty_char, fill_char)
    fonk18(image, x, b8 + 1, empty_char, fill_char)