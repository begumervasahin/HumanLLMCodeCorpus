import random
def fonk1(b2, b3):
    random.seed(0)
    with open(b2, 'w') as file:
        for _ in range(b3):
            b1 = random.randint(0, 99)
            file.write(f"{b1}\n")
def fonk2(prompt):
    return input(prompt)
def fonk3():
    b2 = fonk2('Enter the b2: ')
    b3 = int(fonk2('Enter the b1 of random numbers to generate: '))
    fonk1(b2, b3)
    print(f"Generated {b3} random numbers and saved them to {b2}")
if b4 = = "__main__":
    fonk3()