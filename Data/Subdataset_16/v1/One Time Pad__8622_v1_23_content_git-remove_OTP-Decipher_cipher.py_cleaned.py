import random
from util_function import strxor
def fonk1():
    b1 = int(input("Enter the number of messages: "))
    b2 = []
    for _ in range(b1):
        b2.append(input("Enter message: "))
    return b2
def fonk2(b6, message):
    return strxor(b6, message)
def fonk3(b7):
    b3 = "".join("{:02x}".format(ord(char)) for char in b7)
    print(b3)
def fonk4():
    b2 = fonk1()
    b1 = len(b2)
    b4 = 2 * len(max(b2, b6=len))
    b5 = [hex(random.randint(0, 15)).split('x')[-1] for _ in range(b4)]
    b6 = ''.join(b5)
    print("Number of messages:", b1)
    for message in b2:
        b7 = fonk2(b6, message)
        fonk3(b7)
if b8 = = "__main__":
    fonk4()