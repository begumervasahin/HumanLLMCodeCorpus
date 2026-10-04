
def factorial(x):
    fac = 1
    for i in range(2, x + 1):
        fac *= i
    return fac
def separate_into_chars(num):
    return list(str(num))
def is_special_number(num):
    digits = separate_into_chars(num)
    total = sum(factorial(int(digit)) for digit in digits)
    return total == num
def find_all_special_numbers(max_num):
    special_numbers = []
    for i in range(3, max_num):
        if i % 100000 == 0:
            print(f"Trying i as {i}, so there's another hundred thousand tested")
        if is_special_number(i):
            special_numbers.append(i)
    print(f"Special numbers are {special_numbers}, so there are {len(special_numbers)} that are less than {max_num}.")
    return special_numbers
if __name__ == "__main__":
    find_all_special_numbers(100000000)