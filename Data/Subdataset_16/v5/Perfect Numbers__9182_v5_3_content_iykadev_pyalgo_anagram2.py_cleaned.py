def fonk1(b3, b4):
    def fonk2(s):
        return s.replace(" ", "").lower()
    b1 = fonk2(b3)
    b2 = fonk2(b4)
    return sorted(b1) == sorted(b2)
def fonk3():
    b3 = 'ey edip'
    b4 = 'pide ye'
    b5 = fonk1(b3, b4)
    print(f"'{b3}' and '{b4}' are anagrams: {b5}")
if b6 = = "__main__":
    fonk3()