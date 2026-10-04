import random
from typing import Tuple
from modules import algorithms
b1 = [None] + list('abcdefghijklmnopqrstuvwxyz')
def fonk1(b8: str) -> Tuple[str, str]:
    b2 = [random.choice(b1[1:]) for _ in range(len(b8))]
    b3 = algorithms.alph_pos(b8)
    b4 = algorithms.alph_pos(b2)
    b5 = [(b3[i] + b4[i]) % 26 for i in range(len(b3))]
    b6 = ''.join(b1[num] for num in b5)
    b7 = ''.join(b2)
    return b7, b6
def fonk2():
    b8 = input("Enter b8 data: ").lower()
    if not all(char in b1[1:] for char in b8):
        print("Error: Plaintext contains invalid characters. Only alphabetic characters are allowed.")
    else:
        b2, b6 = fonk1(b8)
        print(f"Your b6 encrypted with the b2: {b2} is: {b6}")
if b9 = = "__main__":
    fonk2()