def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, number):
        if number % b1 = = 0:
            return False
    return True
def fonk2(limit):
    if limit < 2:
        return "Limit should be greater than or equal to 2"
    b2 = []
    for num in range(2, limit + 1):
        if fonk1(num):
            b2.append(num)
    return b2
if b3 = = "__main__":
    print(fonk2(10))