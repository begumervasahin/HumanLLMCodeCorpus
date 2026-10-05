import math
import time
n = input("Check prime numbers up to: ")
start = time.time()
n = int(n)
x = 2
i = 0
primes = []
isprime = True
check = True
with open('output.txt', 'r') as rf:
    for line in rf:
        primes.append(int(line))
    x = int(primes[-1])
while x <= n:
    if len(primes) > i:
        while primes[i] <= math.sqrt(x) and check:
            if x % primes[i] == 0:
                isprime = False
                check = False
            elif i + 1 < len(primes):
                i += 1
            else:
                check = False
        if isprime:
            primes.append(x)
    x += 1
    i = 0
    isprime = True
    check = True
with open('output.txt', 'w') as wf:
    for z in primes:
        wf.write(str(z) + "\n")
end = time.time()
print(str(end - start) + " seconds to calculate")