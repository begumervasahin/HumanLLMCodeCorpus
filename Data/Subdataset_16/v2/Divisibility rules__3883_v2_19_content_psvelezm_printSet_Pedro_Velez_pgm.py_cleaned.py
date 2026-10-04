def fonk1(s):
    b1 = [char for index, char in enumerate(s) if index % 2 == 1]
    b2 = "".join(b1)
    print(f"The input string is: {s}")
    print(f"The characters that have even indexes are: {b2}")
    print(f"The string in reverse order is: {s[::-1]}")
    b3 = s == s[::-1]
    print(f"The string is a palindrome: {b3}")
def fonk2(l, h):
    b4 = {n for n in range(l + 1, h) if n % 7 == 0 and n % 5 != 0}
    print(b4)
if b5 = = "__main__":
    b6 = "11411"
    fonk1(b6)
    a1 = 11
    a2 = 21
    fonk2(a1, a2)