import datetime
fib_cache = {}
def fib(x):
    if x in fib_cache:
        return fib_cache[x]
    if x == 1 or x == 2:
        return 1
    else:
        value = fib(x - 1) + fib(x - 2)
        fib_cache[x] = value
        return value
x = int(input("Enter the number of Fibonacci terms: "))
for i in range(1, x + 1):
    print(f"Fibonacci({i}):", fib(i))
start_time = datetime.datetime.now()
stop_time = datetime.datetime.now()
dt = stop_time - start_time
print("Time taken:", dt)