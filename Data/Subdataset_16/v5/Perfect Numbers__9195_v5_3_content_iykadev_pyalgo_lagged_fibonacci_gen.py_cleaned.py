def fonk1(s, a1, a2, b1 = 10):
    for n in range(b1):
        for b2 in range(len(s)):
            if b2 = = 0:
                b3 = (s[a1 - 1] + s[a2 - 1]) % 10
            elif 0 < b2 < len(s) - 1:
                s[b2] = s[b2 + 1]
            else:
                s[b2] = b3
                print(s[b2])
    return s
def fonk2():
    b4 = [8, 6, 7, 5, 3, 0, 9]
    a1 = 3
    a2 = 7
    b5 = fonk1(b4, a1, a2)
    print(f"Final list: {b5}")
if b6 = = "__main__":
    fonk2()