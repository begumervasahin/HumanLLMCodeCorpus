from util_function import *
import random
def fonk1(b4):
    b1 = int(input())
    for _ in range(b1):
        b4.append(input())
    return b1
def fonk2(b7, message):
    b2 = strxor(b7, message)
    return b2
def fonk3(b2):
    b3 = ""
    for char in b2:
        b3 = b3 + "{:02x}".format(ord(char))
    print(b3)
def fonk4():
    b4 = []
    b1 = fonk1(b4)
    b5 = 2 * len(max(b4, b7 = len))
    b6 = [hex(random.randint(0, 15)).split('x')[-1] for _ in  range(b5)]
    b7 = ''.join(b6)
    print(b1)
    for message in b4:
        b2 = fonk2(b7, message)
        fonk3(b2)
if b8 = = "__main__":
    fonk4()