import doctest
def fonk1(n):
    b1 = n % 3 == 0
    b2 = n % 5 == 0
    if b1 and b2:
        return 'fizzbuzz'
    elif b1:
        return 'fizz'
    elif b2:
        return 'buzz'
    else:
        return str(n)
if b3 = = '__main__':
    doctest.testmod()
    for number in range(1, 101):
        print(fonk1(number))