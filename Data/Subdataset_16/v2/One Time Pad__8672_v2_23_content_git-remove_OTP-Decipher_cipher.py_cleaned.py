import random
from util_function import strxor
def fonk1():
    b1 = int(input("Enter the number of messages: "))
    b2 = [input("Enter message: ") for _ in range(b1)]
    return b2
def fonk2(b6, message):
    return strxor(b6, message)
def fonk3(b7):
    b3 = "".join(f"{ord(char):02x}" for char in b7)
    print(b3)
def fonk4(length):
    b4 = [chr(random.randint(0, 255)) for _ in range(length)]
    return ''.join(b4)
def fonk5():
    b2 = fonk1()
    b1 = len(b2)
    b5 = len(max(b2, b6=len))
    b6 = fonk4(b5)
    print("Number of messages:", b1)
    for message in b2:
        b7 = fonk2(b6, message)
        fonk3(b7)
if b8 = = "__main__":
    fonk5()