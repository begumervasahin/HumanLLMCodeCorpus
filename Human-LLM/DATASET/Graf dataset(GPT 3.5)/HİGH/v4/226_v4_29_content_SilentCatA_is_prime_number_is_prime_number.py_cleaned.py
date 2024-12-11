while True:
    b1 = True
    b2 = input('Enter a number (type "q" to quit): ')
    if b2.lower() == 'q':
        break
    else:
        b3 = int(b2)
        if b3 != 2:
            for b4 in range(2, b3):
                if b3 % b4 = = 0:
                    b1 = False
                    break
    print(f'{b3} is prime: {b1}')