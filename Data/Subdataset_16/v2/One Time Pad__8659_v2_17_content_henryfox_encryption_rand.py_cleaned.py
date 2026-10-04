import random
def fonk1(a1: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(a1))
def fonk2() -> None:
    a1 = 10
    b1 = fonk1(a1)
    print(f"Random number of a1 {a1}: {b1}")
if b2 = = "__main__":
    fonk2()