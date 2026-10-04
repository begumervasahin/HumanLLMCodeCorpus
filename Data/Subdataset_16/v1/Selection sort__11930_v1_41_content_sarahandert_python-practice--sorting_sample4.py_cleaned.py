import random
def fonk1(b1, b2):
    random.seed(0)
    with open(b1, 'w') as f:
        for _ in range(b2):
            f.write(str(random.randrange(0, 100)) + "\b2")
def fonk2():
    b1 = input('Enter the b1: ')
    b2 = int(input('Enter the length of number list: '))
    fonk1(b1, b2)
    print(f"Generated {b2} random numbers and saved to {b1}")
if b3 = = "__main__":
    fonk2()