import argparse
from util_function import *
def fonk1(b12):
    b1 = int(input())
    for _ in range(b1):
        b12.append(input())
    return b1
def fonk2(b1, b12, b13, b14):
    b2 = [char for char in chars]
    for i in range(b1):
        b3 = b12[i]
        b4 = len(b3)
        if b4 % 2 != 0:
            raise Exception("All b3 mod 2 should be 0!")
        b5 = '*' * int(b4 / 2)
        b13.append(b5)
        b14.append([b2 for _ in range(int(b4 / 2))])
def fonk3(text_index1, text_index2, b16, b13, b15, b14):
    for i in range(int(len(b16)/2)):
        b6 = chr(ord(b16[2 * i]) * 16 + ord(b16[2 * i + 1]))
        if b6 in b15:
            b7 = b15[b6]
            b14[text_index1][i] = list_intersection(b14[text_index1][i], b7)
            b14[text_index2][i] = list_intersection(b14[text_index2][i], b7)
def fonk4():
    b8 = argparse.ArgumentParser(description='Process argument full.')
    b8.add_argument('--full', b9 = int, help='whether display all possible characters or not, default is 0')
    b10 = b8.parse_args()
    b11 = b10.full if b10.full is not None else 0
    b12 = []
    b13 = []
    b14 = []
    b15 = {}
    b1 = fonk1(b12)
    fonk2(b1, b12, b13, b14)
    compute_char_xor(b15)
    if b1 < 2:
        raise Exception("OTP is secure if only one b3 is observed!")
    for i in range(b1):
        for j in range(i + 1, b1):
            b16 = hexxor(b12[i], b12[j])
            fonk3(i, j, b16, b13, b15, b14)
    print_result(b14, b11)
if b17 = = "__main__":
    fonk4()