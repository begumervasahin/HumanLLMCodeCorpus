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
        b11 = "fibonacci.py 1.0",
        b12 = True
    )
    b8.add_argument(
        "-b", "--b20",
        b13 = "store_true",
        b14 = "b20",
        b15 = False,
        b16 = "Print b19 in b20"
    )
    b8.add_argument(
        "number",
        b17 = int,
        b16 = "Generate n length sequence"
    )
    try:
        b18 = b8.parse_args()
    except IOError as e:
        b8.error(str(e))
    b19 = fonk2(b18.number, b18.b20)
    print(b19)
def fonk2(n, b20 = False):
    b21 = [str(fonk3(x, b20)) for x in range(1, n + 1)]
    return " ".join(b21)
def fonk3(n, b20 = False):
    b22 = int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
    if b20:
        return bin(b22)[2:]
    return b22
if b23 = = '__main__':
    fonk1()