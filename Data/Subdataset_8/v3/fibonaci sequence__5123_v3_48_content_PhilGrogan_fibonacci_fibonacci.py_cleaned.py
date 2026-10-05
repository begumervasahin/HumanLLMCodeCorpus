def fibonacci_number(n):
    current_number = 1
    previous_number = 1
    for _ in range(n - 2):
        current_number, previous_number = current_number + previous_number, current_number
    return current_number
def ordinal_suffix(i):
    str_i = str(i)
    if str_i[-1] == '1' and (len(str_i) == 1 or str_i[-2] != '1'):
        return 'st'
    elif str_i[-1] == '2' and (len(str_i) == 1 or str_i[-2] != '1'):
        return 'nd'
    elif str_i[-1] == '3' and (len(str_i) == 1 or str_i[-2] != '1'):
        return 'rd'
    else:
        return 'th'
if __name__ == "__main__":
    user_input = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number = fibonacci_number(user_input)
    suffix = ordinal_suffix(user_input)
    print(f"The {user_input}{suffix} Fibonacci number is {fib_number:,d}.")