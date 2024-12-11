while True:
    b1 = True
    b2 = input('> ')
    if b2.lower() == 'q':
        break
    else:
        b2 = int(b2)
        if b2 != 2:
            for b3 in range(2, b2):
                if b2 % b3 = = 0:
                    b1 = False
                    break
    print(f'{b2} is prime: {b1}')