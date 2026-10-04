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
    print("Enter a number to check if it's prime or 'q' to quit.")
    while True:
        b3 = input('> ').strip()
        if b3.lower() == 'q':
            break
        try:
            b1 = int(b3)
            if fonk1(b1):
                print(f'{b1} is a prime number.')
            else:
                print(f'{b1} is not a prime number.')
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.")
if b4 = = "__main__":
    fonk2()