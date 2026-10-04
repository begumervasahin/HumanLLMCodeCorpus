def fonk1(b3):
    if b3 <= 1:
        return False
    for b1 in range(2, int(b3 ** 0.5) + 1):
        if b3 % b1 = = 0:
            return False
    return True
def fonk2():
    while True:
        b2 = input('Enter a b3 (or "q" to quit): ')
        if b2.lower() == 'q':
            break
        try:
            b3 = int(b2)
            if fonk1(b3):
                print(f"{b3} is a prime b3")
            else:
                print(f"{b3} is not a prime b3")
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
if b4 = = "__main__":
    fonk2()