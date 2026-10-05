
nMax = -1
while nMax <= 0:
    user_input = input('Enter a positive integer: ')
    try:
        nMax = int(user_input)
    except ValueError:
        print('Invalid input')
    print()
first_term = 1
second_term = 2
n = 1
while n <= nMax:
    print('%4d: %d' % (n, first_term))
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term
    n += 1
