import datetime
fib_cache = {}
def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = value
    return value
def main():
    try:
        num_terms = int(input("Enter the number of Fibonacci terms: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    start_time = datetime.datetime.now()
    for i in range(1, num_terms + 1):
        print(f"{i}: {fibonacci(i)}")
    stop_time = datetime.datetime.now()
    elapsed_time = stop_time - start_time
    print("Time taken:", elapsed_time)
if __name__ == '__main__':
    main()