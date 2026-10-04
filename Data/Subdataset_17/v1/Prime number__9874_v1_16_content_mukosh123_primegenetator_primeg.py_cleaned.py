def primeGenerator(num):
    if type(num) != int:
        return 'wrong arg'
    if num < 0 or type(num) != int:
        return 'wrong arg'
    prime_list = []
    for i in range(1, num + 1):
        prime = True
        j = 2
        while j < i:
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            prime_list.append(i)
    return prime_list
if __name__ == "__main__":
    limit = 10
    primes = primeGenerator(limit)
    print("Prime numbers up to {}: {}".format(limit, primes))