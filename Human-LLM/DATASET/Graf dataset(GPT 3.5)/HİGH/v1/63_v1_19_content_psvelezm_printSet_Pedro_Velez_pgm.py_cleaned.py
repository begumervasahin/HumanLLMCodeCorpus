def fonk1(b4):
    b1 = list(b4)
    b2 = [char for index, char in enumerate(b1) if index % 2 == 0]
    b3 = "".join(b2)
    print("The input string is:", b4)
    print("The characters that have even indexes are:", b3)
    print("The string in reverse order is:", b4[::-1])
    if b4 = = b4[::-1]:
        print("The string is a palindrome: True")
    else:
        print("The string is a palindrome: False")
def fonk2(L, H):
    b5 = []
    for i in range(L + 1, H):
        if i % b6 = = 0 and i % 5 != 0:
            b5.append(i)
    b7 = set(b5)
    print(b7)
fonk1("11411")
fonk2(11, 21)