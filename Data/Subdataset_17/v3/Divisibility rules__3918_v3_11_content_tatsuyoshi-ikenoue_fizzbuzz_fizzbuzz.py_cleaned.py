import doctest
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return str(n)
if __name__ == '__main__':
    doctest.testmod()
    for number in range(1, 101):
        print(fizzbuzz(number))