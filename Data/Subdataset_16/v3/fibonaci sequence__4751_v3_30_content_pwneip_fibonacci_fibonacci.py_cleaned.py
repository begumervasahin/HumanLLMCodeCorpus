import argparse
from math import sqrt
b1 = "PwnEIP"
b2 = "Copyright 2007, The Cogent Project"
b3 = "GPL"
b4 = "1.0"
b5 = "PwnEIP"
b6 = "pwneip@gmail.com"
b7 = "Production"
def fonk1(n):
    b8 = (1 + sqrt(5)) / 2
    b9 = (1 - sqrt(5)) / 2
    return int((b8**n - b9**n) / sqrt(5))
def fonk2(number, b10 = False):
    b11 = []
    for x in range(1, number + 1):
        b12 = fonk1(x)
        if b10:
            b11.append(bin(b12)[2:])
        else:
            b11.append(str(b12))
    return b11
def fonk3():
    b13 = argparse.ArgumentParser(description='Generate Fibonacci b11')
    b13.add_argument(
        "-b", "--b10",
        b14 = "store_true",
        b15 = "Print output in b10"
    )
    b13.add_argument(
        "number",
        b16 = int,
        b15 = "Generate n length b11"
    )
    b17 = b13.parse_args()
    b11 = fonk2(b17.number, b17.b10)
    print(" ".join(b11))
if b18 = = '__main__':
    fonk3()