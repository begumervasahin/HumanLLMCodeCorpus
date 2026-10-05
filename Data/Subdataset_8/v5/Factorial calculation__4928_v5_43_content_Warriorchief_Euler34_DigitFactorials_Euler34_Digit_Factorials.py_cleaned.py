
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result
def separate_into_chars(num):
    return list(str(num))
def is_special_number(num):
    digits = separate_into_chars(num)
    digit_factorial_sum = sum(factorial(int(char)) for char in digits)
    return digit_factorial_sum == num
def find_all_special_numbers(max_num):
    special_numbers = []
    i = 3
    while i < max_num:
        if i % 100000 == 0:
            print("Testing another hundred thousand at", i)
        if is_special_number(i):
            special_numbers.append(i)
        i += 1
    print("Special numbers:", special_numbers)
    print("Count:", len(special_numbers))
    return special_numbers
if __name__ == "__main__":
    max_number = 100000000
    find_all_special_numbers(max_number)