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
    if b1 <= 1:
        return False
    elif b2 % b1 = = 0:
        return True
    return fonk4(b2, b1 - 1)
def fonk5(b2):
    if b2 < 2:
        return False
    return not fonk4(b2, int(b2 ** 0.5))
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
    if b2 = = 1:
        hanoi.move(src, dest)
        return
    fonk8(hanoi, b2 - 1, src, temp, dest)
    hanoi.move(src, dest)
    fonk8(hanoi, b2 - 1, temp, dest, src)
def fonk9(char_list, b2):
    if b2 = = 0:
        return
    fonk10(char_list, "", len(set(char_list)), b2)
def fonk10(char_list, prefix, b2, b3):
    if b3 = = 0:
        print(prefix)
        return
    for b1 in range(b2):
        b4 = prefix + char_list[b1]
        fonk10(char_list, b4, b2, b3 - 1)
def fonk11(char_list, b2):
    if b2 = = 0:
        return
    fonk12(char_list, "", b2)
def fonk12(char_list, prefix, b2):
    if b2 = = 0:
        print(prefix)
        return
    for b1, char in enumerate(char_list):
        b4 = prefix + char
        fonk12(char_list[:b1] + char_list[b1 + 1:], b4, b2 - 1)
def fonk13(b2):
    b5 = []
    if b2 > 0:
        fonk14([""] * 2 * b2, 0, b2, 0, 0, b5)
    return b5
def fonk14(curr, pos, b2, open, b6, b5):
    if b6 = = b2:
        b5.append(fonk1(curr))
        return
    if open > b6:
        curr[pos] = ')'
        fonk14(curr, pos + 1, b2, open, b6 + 1, b5)
    if open < b2:
        curr[pos] = '('
        fonk14(curr, pos + 1, b2, open + 1, b6, b5)
def fonk15(b2, b3):
    if b2 < 0 or b3 < 0:
        return
    fonk16(b2, b3, "")
def fonk16(b2, b3, prefix):
    if b2 = = 0 and b3 == 0:
        print(prefix)
        return
    if b2 > 0:
        fonk16(b2 - 1, b3, prefix + 'r')
    if b3 > 0:
        fonk16(b2, b3 - 1, prefix + 'u')
def fonk17(b11, start):
    x, b7 = start
    fonk18(b11, x, b7, '.', '*')
def fonk18(b11, x, b7, empty_char, fill_char):
    b8 = len(b11)
    b9 = len(b11[0])
    if x < 0 or x >= b8 or b7 < 0 or b7 >= b9 or b11[x][b7] != empty_char:
        return
    b11[x][b7] = fill_char
    fonk18(b11, x - 1, b7, empty_char, fill_char)
    fonk18(b11, x + 1, b7, empty_char, fill_char)
    fonk18(b11, x, b7 - 1, empty_char, fill_char)
    fonk18(b11, x, b7 + 1, empty_char, fill_char)
if b10 = = "__main__":
    print("Sum of numbers up to 5:", sum_of_numbers(5))
    print("Is 3 a prime number?", fonk5(3))
    print("Factorial of 5:", fonk6(5))
    print("Value of e^2 calculated up to 5 terms:", fonk7(5, 2))
    print("Printing numbers from 1 to 5:")
    fonk2(5)
    print("Printing numbers from 5 to 1:")
    fonk3(5)
    print("Printing sequences of length 3 from 'hello':")
    fonk9(['h', 'e', 'l', 'l', 'o'], 3)
    print("Generating parentheses combinations for 3 pairs:")
    for combination in fonk13(3):
        print(combination)
    print("Possible paths from (0,0) to (2,2):")
    fonk15(2, 2)
    b11 = [
        ['.', '.', '.', '.', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '*', '.', '*', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '.', '.', '.', '.']
    ]
    print("Flood fill from (2,2):")
    fonk17(b11, (2, 2))
    for row in b11:
        print(''.join(row))