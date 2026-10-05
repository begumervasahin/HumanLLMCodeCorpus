import doctest
def fizzbuzz(n):
    divisible_by_3 = n % 3 == 0
    divisible_by_5 = n % 5 == 0
    if divisible_by_3 and divisible_by_5:
        return 'fizzbuzz'
    elif divisible_by_3:
        return 'fizz'
    elif divisible_by_5:
        return 'buzz'
    else:
        return str(n)
if __name__ == '__main__':
    doctest.testmod()
    for number in range(1, 101):
        print(fizzbuzz(number))