import math
import time
n = input("Check prime numbers: ")
start = time.time()
n = int(n)
x = 2
i = 0
primes = []
isprime = True
check = True
with open('output.txt','r') as rf:
    for line in rf:
        primes.append(int(line))
    x = int(primes[-1])
while x <= n:
    if len(primes) > i:
        while primes[i] <= math.sqrt(x) and check:
            if x % primes[i] == 0:
                isprime = False
                check = False
            elif i+1 < len(primes):
                i += 1
            else:
                check = False
        if isprime:
            primes.append(x)
    x += 1
    i = 0
    isprime = True
    check = True
'''
while x <= n:
    while i < math.sqrt(x):
        if x%i == 0:
            isprime = False
            i = x
        else:
            i += 1
    if isprime:
        primes.append(x)
    x += 1
    i = 2
    isprime = True
'''
end = time.time()
with open('output.txt', 'w') as wf:
    for z in primes:
        wf.write(str(z)+ "\n")
print(str(end-start) + " seconds to calculate")