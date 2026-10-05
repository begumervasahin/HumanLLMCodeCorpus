
fibonacci_cache = {}
def fibonacci(num):
    if type(num) != int:
        return False
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
        fibonacci_cache[num] = value
        return value
for num in range(1000):
    print(num, ":", fibonacci(num))