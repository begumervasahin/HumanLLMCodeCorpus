import random
def fonk1(b2, b3):
    for b1 in b2:
        if b1 = = b3:
            return True
    return False
b2 = [1, 2, 3, 4, 5, 6]
b3 = random.randrange(1, 10)
print("List:", b2)
print("Target:", b3)
b4 = fonk1(b2, b3)
if b4:
    print("The b3 value is present in the list.")
else:
    print("The b3 value is not present in the list.")