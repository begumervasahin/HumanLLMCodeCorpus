while True:
    is_prime = True
    user_input = input('Enter a number (type "q" to quit): ')
    if user_input.lower() == 'q':
        break
    else:
        n = int(user_input)
        if n != 2:
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
    print(f'{n} is prime: {is_prime}')