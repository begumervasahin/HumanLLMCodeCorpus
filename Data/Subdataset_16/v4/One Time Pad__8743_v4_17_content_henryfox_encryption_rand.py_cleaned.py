import random
def fonk1(digits):
    b1 = [str(random.randint(0, 9)) for _ in range(digits)]
    return "".join(b1)
print(fonk1(5))
