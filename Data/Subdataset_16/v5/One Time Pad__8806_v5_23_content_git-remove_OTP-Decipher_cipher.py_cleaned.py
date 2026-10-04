import random
from util_function import strxor
def fonk1():
    b1 = []
    b2 = int(input("Enter the number of messages: "))
    for _ in range(b2):
        b1.append(input("Enter message: "))
    return b1
def fonk2(b6, message):
    return strxor(b6, message)
def fonk3(b7):
    b3 = "".join(f"{ord(char):02x}" for char in b7)
    print(b3)
def fonk4(length):
    return ''.join(random.choice("0123456789abcdef") for _ in range(length))
def fonk5():
    b1 = fonk1()
    b4 = max(len(message) for message in b1)
    b5 = 2 * b4
    b6 = fonk4(b5)
    print(f"Number of messages: {len(b1)}")
    for message in b1:
        b7 = fonk2(b6, message)
        fonk3(b7)
if b8 = = "__main__":
    fonk5()