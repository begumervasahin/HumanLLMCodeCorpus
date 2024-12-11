from math import sqrt
import argparse
b1 = "PwnEIP"
b2 = "Copyright 2007, The Cogent Project"
b3 = "GPL"
b4 = "1.0"
b5 = "PwnEIP"
b6 = "pwneip@gmail.com"
b7 = "Production"
def fonk1():
    b8 = argparse.ArgumentParser(
        b9 = 'Generate Fibonacci sequence',
        b10 = "fibonacci.py [-b] number",
        b11 = True
    )
    b8.add_argument(
        "-b", "--b19",
        b12 = "store_true",
        b13 = "b19",
        b14 = False,
        b15 = "Print b18 in b19"
    )
    b8.add_argument(
        "number",
        b16 = int,
        b15 = "Generate n length sequence"
    )
    b17 = b8.parse_args()
    b18 = fonk2(b17.number, b17.b19)
    print(b18)
def fonk2(n, b19 = False):
    b20 = []
    for x in range(1, n + 1):
        b21 = fonk3(x)
        if b19:
            b20.append(bin(b21)[2:])
        else:
            b20.append(repr(b21))
    return " ".join(b20)
def fonk3(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
if b22 = = '__main__':
    fonk1()