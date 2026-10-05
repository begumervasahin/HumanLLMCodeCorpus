while True:
    is_prime = True
    n = input('> ')
    if n.lower() == 'q':
        break
    else:
        n = int(n)
        if n != 2:
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
    print(f'{n} is prime: {is_prime}')
