import random
def fonk1(b1, b2):
    for i in range(len(b1)):
        if b1[i] == b2:
            return True
    return False
b1 = [1, 2, 3, 4, 5, 6]
b2 = random.randrange(1, 10)
print("List:", b1)
print("Target:", b2)
b3 = fonk1(b1, b2)
if b3:
    print("The b2 value is present in the list.")
else:
    print("The b2 value is not present in the list.")