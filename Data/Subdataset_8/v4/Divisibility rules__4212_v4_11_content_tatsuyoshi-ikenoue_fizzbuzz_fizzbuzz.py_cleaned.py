import doctest
def fizzbuzz(n):
    return str(n)
if __name__ == '__main__':
    doctest.testmod()
    for n in range(100):
        print(fizzbuzz(n))