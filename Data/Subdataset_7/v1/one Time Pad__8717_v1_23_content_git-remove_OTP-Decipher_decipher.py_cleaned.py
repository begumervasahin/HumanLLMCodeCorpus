
def fonk1(a, b):
    return [val for val in a if val in b]
def fonk2(b15):
    pass
def fonk3(a, b):
    pass
def fonk4(b14, b11):
    pass
import argparse
def fonk5(b12):
    b1 = int(input())
    for _ in range(b1):
        b12.append(input())
    return b1
def fonk6(b1, b12, b13, b14):
    b2 = [char for char in chars]
    for i in range(b1):
        b3 = b12[i]
        b4 = len(b3)
        if b4 % 2 != 0:
            raise Exception("All b3 mod 2 should be 0!")
        b5 = '*' * int(b4 / 2)
        b13.append(b5)
        b14.append([b2 for _ in range(int(b4 / 2))])
def fonk7(text_index1, text_index2, b16, b13, b15, b14):
    for i in range(int(len(b16)/2)):
        b6 = chr(ord(b16[2 * i]) * 16 + ord(b16[2 * i + 1]))
        if b6 in b15:
            b7 = b15[b6]
            b14[text_index1][i] = fonk1(b14[text_index1][i], b7)
            b14[text_index2][i] = fonk1(b14[text_index2][i], b7)
def fonk8():
    b8 = argparse.ArgumentParser(description='Process argument full.')
    b8.add_argument('--full', b9 = int, help='whether display all possible characters or not, default is 0')
    b10 = b8.parse_args()
    if b10.full is not None:
        b11 = int(b10.full)
    else:
        b11 = 0
    b12 = []
    b13 = []
    b14 = []
    b15 = {}
    b1 = fonk5(b12)
    fonk6(b1, b12, b13, b14)
    fonk2(b15)
    if b1 < 2:
        raise Exception("OPT is secure if only one b3 is observed!")
    for i in range(b1):
        for j in range(i + 1, b1):
            b16 = fonk3(b12[i], b12[j])
            fonk7(i, j, b16, b13, b15, b14)
    fonk4(b14, b11)
if b17 = = "__main__":
    fonk8()