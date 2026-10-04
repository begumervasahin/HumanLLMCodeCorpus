def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(n):
    if n < 2:
        return "Number should be greater than or equal to 2"
    b2 = [num for num in range(2, n + 1) if fonk1(num)]
    return b2
if b3 = = "__main__":
    print(fonk2(10))