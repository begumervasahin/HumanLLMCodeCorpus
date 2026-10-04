import random
from util_function import strxor
def fonk1():
    b1 = int(input("Enter the number of messages: "))
    return [input("Enter message: ") for _ in range(b1)]
def fonk2(b5, message):
    return strxor(b5, message)
def fonk3(b6):
    b2 = "".join(f"{ord(char):02x}" for char in b6)
    print(b2)
def fonk4(length):
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))
def fonk5():
    b3 = fonk1()
    b4 = max(len(message) for message in b3)
    b5 = fonk4(b4)
    print("Number of messages:", len(b3))
    for message in b3:
        b6 = fonk2(b5, message)
        fonk3(b6)
if b7 = = "__main__":
    fonk5()