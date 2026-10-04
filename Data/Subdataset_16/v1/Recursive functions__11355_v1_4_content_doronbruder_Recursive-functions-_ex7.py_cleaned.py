def fonk1(List):
    return ''.join(List)
def fonk2(b2):
    if b2 >= 1:
        fonk2(b2 - 1)
        print(b2)
    else:
        return
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
        b5 = b9 + char
        fonk12(char_list[:b1] + char_list[b1 + 1:], b5, b2 - 1)
def fonk13(b2):
    b6 = [""] * 2 * b2
    b7 = []
    if b2 > 0:
        fonk14(b6, 0, b2, 0, 0, b7)
    return b7
def fonk14(b6, pos, b2, open, b8, b7):
    if b8 = = b2:
        b7.append(fonk1(b6))
        return
    else:
        if open > b8:
            b6[pos] = ')'
            fonk14(b6, pos + 1, b2, open, b8 + 1, b7)
        if open < b2:
            b6[pos] = '('
            fonk14(b6, pos + 1, b2, open + 1, b8, b7)
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
def fonk17(b14, start):
    x, b10 = start
    fonk18(b14, x, b10, '.', '*')
def fonk18(b14, x, b10, empty_char, full_char):
    b11 = len(b14)
    b12 = len(b14[0])
    if x < 0 or x >= b11 or b10 < 0 or b10 >= b12 or b14[x][b10] != empty_char:
        return
    b14[x][b10] = full_char
    fonk18(b14, x - 1, b10, empty_char, full_char)
    fonk18(b14, x, b10 - 1, empty_char, full_char)
    fonk18(b14, x + 1, b10, empty_char, full_char)
    fonk18(b14, x, b10 + 1, empty_char, full_char)
if b13 = = "__main__":
    print("Sum of numbers up to 5:", sumOfNumbers(5))
    print("Is 3 a prime number?", fonk5(3))
    print("Factorial of 5:", fonk6(5))
    print("Value of e^2 calculated up to 5 terms:", fonk7(5, 2))
    print("Printing numbers from 1 to 5:")
    fonk2(5)
    print("Printing numbers from 5 to 1:")
    fonk3(5)
    print("Reversing the string 'hello':")
    fonk9(['h', 'e', 'l', 'l', 'o'], 3)
    print("Generating parentheses combinations for 3 pairs:")
    for combination in fonk13(3):
        print(combination)
    print("Possible paths from (0,0) to (2,2):")
    fonk15(2, 2)
    b14 = [
        ['.', '.', '.', '.', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '*', '.', '*', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '.', '.', '.', '.']
    ]
    print("Flood fill from (2,2):")
    fonk17(b14, (2, 2))
    for row in b14:
        print(''.join(row))