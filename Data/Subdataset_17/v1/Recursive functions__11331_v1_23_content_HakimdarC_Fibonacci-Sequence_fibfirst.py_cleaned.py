import datetime
fib_cache = {}
def fib(x):
    if x in fib_cache:
        return fib_cache[x]
    if x == 1:
        value = 1
    elif x == 2:
        value = 1
    else:
        value = fib(x - 1) + fib(x - 2)
    fib_cache[x] = value
    return value
x = int(input("Give the number of Fibonacci terms: "))
start_time = datetime.datetime.now()
for i in range(1, x + 1):
    print(i, ":", fib(i))
stop_time = datetime.datetime.now()
dt = stop_time - start_time
print("Time taken:", dt)