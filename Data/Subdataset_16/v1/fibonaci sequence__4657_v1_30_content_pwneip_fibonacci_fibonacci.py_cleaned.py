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
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
def fonk2():
    b8 = argparse.ArgumentParser(description='Generate Fibonacci sequence')
    b8.add_argument(
        "-b", "--binary",
        b9 = "store_true",
        b10 = "Print b13 in binary"
    )
    b8.add_argument(
        "number",
        b11 = int,
        b10 = "Generate n length sequence"
    )
    b12 = b8.parse_args()
    b13 = ""
    for x in range(1, b12.number + 1):
        if b12.binary:
            b13 += bin(fonk1(x))[2:] + " "
        else:
            b13 += repr(fonk1(x)) + " "
    print(b13)
if b14 = = '__main__':
    fonk2()