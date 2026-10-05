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
    str_i = str(i)
    if str_i[-1] == '1' and str_i[-2] != '1':
        return 'st'
    elif str_i[-1] == '2' and str_i[-2] != '1':
        return 'nd'
    elif str_i[-1] == '3' and str_i[-2] != '1':
        return 'rd'
    else:
        return 'th'
if __name__ == "__main__":
    user_input = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number = fibonacci_number(user_input)
    suffix = ordinal_suffix(user_input)
    print(f"The {user_input}{suffix} Fibonacci number is {fib_number:,d}.")