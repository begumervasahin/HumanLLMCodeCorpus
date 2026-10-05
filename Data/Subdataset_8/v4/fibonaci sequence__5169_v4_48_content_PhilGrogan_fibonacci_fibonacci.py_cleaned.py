
def fibonacci_and_suffix(n):
    current_number = 1
    previous_number = 1
    for _ in range(n - 1):
        total = current_number + previous_number
        previous_number = current_number
        current_number = total
    suffix = 'th'
    str_n = str(n)
    if str_n[-1] == '1' and (len(str_n) == 1 or str_n[-2] != '1'):
        suffix = 'st'
    elif str_n[-1] == '2' and (len(str_n) == 1 or str_n[-2] != '1'):
        suffix = 'nd'
    elif str_n[-1] == '3' and (len(str_n) == 1 or str_n[-2] != '1'):
        suffix = 'rd'
    return current_number, suffix
if __name__ == "__main__":
    user_input = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
    fib_number, suffix = fibonacci_and_suffix(user_input)
    print(f"The {user_input}{suffix} number of the Fibonacci sequence is {fib_number:,d}.")