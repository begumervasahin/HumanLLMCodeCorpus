from difflib import ndiff, restore
def fonk1(b1, b2):
    return list(ndiff(b1, b2))
def fonk2(b3, which):
    return ''.join(restore(b3, which))
def fonk3():
    b1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
    b2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
    b3 = fonk1(b1, b2)
    b4 = fonk2(b3, 1)
    b5 = fonk2(b3, 2)
    print(b4, b6 = "")
    print(b5, b6 = "")
if b7 = = "__main__":
    fonk3()