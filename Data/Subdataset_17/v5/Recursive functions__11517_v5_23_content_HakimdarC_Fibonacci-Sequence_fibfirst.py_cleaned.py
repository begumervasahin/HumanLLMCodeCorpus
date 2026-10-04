import datetime
fib_cache = {}
def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fib(n - 1) + fib(n - 2)
        fib_cache[n] = value
    return value
def main():
    num_terms = int(input("Give the number of Fibonacci terms: "))
    start_time = datetime.datetime.now()
    for i in range(1, num_terms + 1):
        print(f"{i}: {fib(i)}")
    stop_time = datetime.datetime.now()
    elapsed_time = stop_time - start_time
    print(f"Elapsed time: {elapsed_time}")
if __name__ == "__main__":
    main()