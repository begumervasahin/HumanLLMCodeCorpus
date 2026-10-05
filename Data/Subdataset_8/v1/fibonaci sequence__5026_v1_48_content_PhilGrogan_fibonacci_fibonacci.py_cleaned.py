
def fibonacci_number(n):
    current_number = 1
    previous_number = 1
    total = 0
    for _ in range(n - 1):
        total = current_number + previous_number
        previous_number = current_number
        current_number = total
    return current_number
def ordinal_suffix(i):
    li = list(str(i))
    if li[-1] == '1' and li[-2] != '1':
        return 'st'
    elif li[-1] == '2' and li[-2] != '1':
        return 'nd'
    elif li[-1] == '3' and li[-2] != '1':
        return 'rd'
    else:
        return 'th'
if __name__ == "__main__":
    i = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number = fibonacci_number(i)
    suffix = ordinal_suffix(i)
    print(f"{fib_number:,d} is the {i:,d}{suffix} number of the Fibonacci sequence.")