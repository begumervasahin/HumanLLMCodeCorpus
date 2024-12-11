def fonk1(b4):
    if b4 < 2:
        return False
    for b1 in range(2, int(b4 ** 0.5) + 1):
        if b4 % b1 = = 0:
            return False
    return True
if b2 = = "__main__":
    while True:
        b3 = input('Enter a number (type "q" to quit): ')
        if b3.lower() == 'q':
            break
        else:
            b4 = int(b3)
            b5 = fonk1(b4)
            print(f'{b4} is b5: {b5}')