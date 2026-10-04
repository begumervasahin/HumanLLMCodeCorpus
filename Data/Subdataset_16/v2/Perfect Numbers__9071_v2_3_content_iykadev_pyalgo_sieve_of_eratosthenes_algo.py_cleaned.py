def fonk1(limit: int):
    b1 = set()
    for number in range(2, limit + 1):
        if number not in b1:
            yield number
            b1.update(range(number * number, limit + 1, number))
def fonk2() -> None:
    b2 = list(fonk1(100))
    print(b2)
if b3 = = "__main__":
    fonk2()