def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(a1):
    if a1 < 2:
        return "Number should be greater than or equal to 2"
    b2 = []
    for num in range(2, a1 + 1):
        if fonk1(num):
            b2.append(num)
    return b2
def fonk3():
    a1 = 10
    b3 = fonk2(a1)
    print(f"Prime numbers up to {a1}: {b3}")
if b4 = = "__main__":
    fonk3()