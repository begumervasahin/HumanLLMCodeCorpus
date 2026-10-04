import random
from modules import algorithms
def fonk1(length):
    b1 = 'abcdefghijklmnopqrstuvwxyz'
    return [random.choice(b1) for _ in range(length)]
def fonk2(b6, b7):
    b2 = algorithms.alph_pos(list(b6))
    b3 = algorithms.alph_pos(b7)
    b4 = [
        (b2[i] + b3[i]) % 26
        for i in range(len(b2))
    ]
    b5 = algorithms.num_alph(b4)
    return "".join(b5)
def fonk3():
    b6 = input("Enter b6 data: ")
    b7 = fonk1(len(b6))
    b5 = fonk2(b6, b7)
    print(f"Your b5 encrypted with the b7: {''.join(b7)} is: {b5}")
if b8 = = "__main__":
    fonk3()