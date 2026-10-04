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
    return " ".join(b11)
def fonk3():
    b13 = argparse.ArgumentParser(
        b14 = 'Generate Fibonacci sequence',
        b15 = "fibonacci.py [-b] number"
    )
    b13.add_argument(
        "-b", "--b10",
        b16 = "store_true",
        b17 = "Print b11 in b10"
    )
    b13.add_argument(
        "number",
        b18 = int,
        b17 = "Generate n length sequence"
    )
    b19 = b13.parse_args()
    b11 = fonk2(b19.number, b19.b10)
    print(b11)
if b20 = = '__main__':
    fonk3()