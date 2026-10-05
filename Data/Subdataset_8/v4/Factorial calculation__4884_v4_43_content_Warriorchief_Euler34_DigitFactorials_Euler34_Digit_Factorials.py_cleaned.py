
def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac
def separate_into_chars(num):
    return list(str(num))
def is_special_number(num):
    chars = separate_into_chars(num)
    total = sum(factorial(int(char)) for char in chars)
    return total == num
def find_all_special_numbers(max_num):
    special_numbers = []
    i = 3
    while i < max_num:
        if i % 100000 == 0:
            print("Trying i as", i, "so there's another hundred thousand tested")
        if is_special_number(i):
            special_numbers.append(i)
        i += 1
    print("Special numbers:", special_numbers)
    print("Count:", len(special_numbers))
    return special_numbers
if __name__ == "__main__":
    max_number = 100000000
    find_all_special_numbers(max_number)