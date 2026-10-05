def fonk1(b2):
    if b2 < 2:
        return False
    for b1 in range(2, int(b2 ** 0.5) + 1):
        if b2 % b1 = = 0:
            return False
    return True
def fonk2():
    while True:
        b2 = input('> ')
        if b2.lower() == 'q':
            break
        else:
            try:
                b2 = int(b2)
                b3 = fonk1(b2)
                print(f'{b2} is prime: {b3}')
            except ValueError:
                print("Invalid input. Please enter a valid integer or 'q' to quit.")
if b4 = = "__main__":
    fonk2()