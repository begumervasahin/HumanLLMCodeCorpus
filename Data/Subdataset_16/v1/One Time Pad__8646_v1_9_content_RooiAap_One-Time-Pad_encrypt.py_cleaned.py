import random
from modules import algorithms
b1 = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def fonk1(b9: str) -> Tuple[str, str]:
    b2 = [random.choice(b1[1:]) for _ in range(len(b9))]
    b3 = algorithms.alph_pos(b9)
    b4 = algorithms.alph_pos(b2)
    b5 = [(b3[p] + b4[p]) % 26 for p in range(len(b3))]
    b6 = ''.join(b1[num] for num in b5)
    b7 = ''.join(b2)
    return b7, b6
if b8 = = "__main__":
    b9 = input("Enter b9 data: ").lower()
    if not all(char in b1[1:] for char in b9):
        print("Error: Plaintext contains invalid characters. Only alphabetic characters are allowed.")
    else:
        b2, b6 = fonk1(b9)
        print(f"Your b6 encrypted with the b2: {b2} is: {b6}")