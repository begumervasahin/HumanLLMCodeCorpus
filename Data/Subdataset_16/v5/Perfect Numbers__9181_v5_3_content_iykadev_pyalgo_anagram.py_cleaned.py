def fonk1(b1, b2):
    b1 = b1.replace(" ", "").lower()
    b2 = b2.replace(" ", "").lower()
    return sorted(b1) == sorted(b2)
def fonk2():
    b3 = 'ey edip'
    b4 = 'pide ye'
    b5 = fonk1(b3, b4)
    print(f"'{b3}' and '{b4}' are anagrams: {b5}")
if b6 = = "__main__":
    fonk2()