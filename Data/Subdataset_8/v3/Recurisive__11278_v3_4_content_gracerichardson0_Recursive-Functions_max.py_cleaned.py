def get_positive_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            n = int(user_input)
            if n > 0:
                return n
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a positive integer.')
nMax = get_positive_integer_input('Enter a positive integer: ')
first_term = 1
second_term = 2
n = 1
while n <= nMax:
    print(f'{n:4d}: {first_term}')
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term
    n += 1
