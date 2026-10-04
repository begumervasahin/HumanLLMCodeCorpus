def print_string_properties(s):
    even_chars = [char for index, char in enumerate(s) if index % 2 == 1]
    even_string = "".join(even_chars)
    print(f"The input string is: {s}")
    print(f"The characters that have even indexes are: {even_string}")
    print(f"The string in reverse order is: {s[::-1]}")
    is_palindrome = s == s[::-1]
    print(f"The string is a palindrome: {is_palindrome}")
def print_set(l, h):
    numbers = {n for n in range(l + 1, h) if n % 7 == 0 and n % 5 != 0}
    print(numbers)
if __name__ == "__main__":
    test_string = "11411"
    print_string_properties(test_string)
    lower_bound = 11
    upper_bound = 21
    print_set(lower_bound, upper_bound)