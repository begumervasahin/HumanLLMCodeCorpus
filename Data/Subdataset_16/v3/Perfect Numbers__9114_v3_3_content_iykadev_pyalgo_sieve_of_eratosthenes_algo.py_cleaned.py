def fonk1(a1: int):
    b1 = set()
    for number in range(2, a1 + 1):
        if number not in b1:
            yield number
            b1.update(range(number * number, a1 + 1, number))
def fonk2() -> None:
    a1 = 100
    b2 = list(fonk1(a1))
    print(f"Prime numbers up to {a1}: {b2}")
if b3 = = "__main__":
    fonk2()