import difflib
def fonk1(str1, str2):
    b1 = str1.splitlines(keepends=True)
    b2 = str2.splitlines(keepends=True)
    b3 = difflib.Differ()
    b4 = b3.ndiff(b1, b2)
    print(''.join(b4), b5 = "")
b6 = 'one\ntwo\nthree\n'
b7 = 'ore\ntree\nemu\n'
fonk1(b6, b7)