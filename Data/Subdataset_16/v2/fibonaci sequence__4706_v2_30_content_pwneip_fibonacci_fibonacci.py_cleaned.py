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
def fonk2():
    b10 = argparse.ArgumentParser(description='Generate Fibonacci sequence')
    b10.add_argument(
        "-b", "--binary",
        b11 = "store_true",
        b12 = "Print b15 in binary"
    )
    b10.add_argument(
        "number",
        b13 = int,
        b12 = "Generate n length sequence"
    )
    b14 = b10.parse_args()
    b15 = []
    for x in range(1, b14.number + 1):
        b16 = fonk1(x)
        if b14.binary:
            b15.append(bin(b16)[2:])
        else:
            b15.append(str(b16))
    print(" ".join(b15))
if b17 = = '__main__':
    fonk2()