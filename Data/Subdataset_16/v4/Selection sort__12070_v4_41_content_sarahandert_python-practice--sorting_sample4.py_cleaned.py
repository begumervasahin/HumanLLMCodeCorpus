import random
def fonk1(b2, b3):
    random.seed(0)
    with open(b2, 'w') as f:
        for _ in range(b3):
            f.write(f"{random.randint(0, 99)}\b3")
if b1 = = "__main__":
    b2 = input('Enter the b2: ')
    b3 = int(input('Enter the length of number list: '))
    fonk1(b2, b3)