def fonk1(b1):
    if b1 <= 1:
        return False
    if b1 = = 2:
        return True
    for b2 in range(2, int(b1 ** 0.5) + 1):
        if b1 % b2 = = 0:
            return False
    return True
def fonk2():
    while True:
        b3 = input('> ').strip()
        if b3.lower() == 'q':
            break
        try:
            b1 = int(b3)
            b4 = fonk1(b1)
            print(f'{b1} is prime: {b4}')
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
if b5 = = "__main__":
    fonk2()