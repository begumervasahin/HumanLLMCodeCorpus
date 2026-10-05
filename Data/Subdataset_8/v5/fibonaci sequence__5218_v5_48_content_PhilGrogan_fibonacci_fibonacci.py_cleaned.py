def calculate_fibonacci_and_suffix(n):
    current = 1
    previous = 1
    for _ in range(n - 1):
        total = current + previous
        previous = current
        current = total
    suffix = 'th'
    str_n = str(n)
    if str_n[-2:] not in ('11', '12', '13'):
        if str_n[-1] == '1':
            suffix = 'st'
        elif str_n[-1] == '2':
            suffix = 'nd'
        elif str_n[-1] == '3':
            suffix = 'rd'
    return current, suffix
if __name__ == "__main__":
    user_input = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number, suffix = calculate_fibonacci_and_suffix(user_input)
    print(f"The {user_input}{suffix} number of the Fibonacci sequence is {fib_number:,d}.")