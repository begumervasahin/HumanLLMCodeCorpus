def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, num):
        if num % b1 = = 0:
            return False
    else:
        return True
def fonk2(n):
    if n < 2:
        return "Number should be greater than or equal 2"
    b2 = []
    for num in range(2, n+1):
        if fonk1(num):
            b2.append(num)
    return b2
if b3 = = "__main__":
    print(fonk2(10))