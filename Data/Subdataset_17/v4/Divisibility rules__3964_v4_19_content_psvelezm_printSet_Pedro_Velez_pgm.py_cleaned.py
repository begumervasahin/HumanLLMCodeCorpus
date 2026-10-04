def print_string_properties(s):
    even_chars = [s[i] for i in range(len(s)) if i % 2 == 0]
    even_string = "".join(even_chars)
    print(f"The input string is: {s}")
    print(f"The characters at even indexes are: {even_string}")
    print(f"The string in reverse order is: {s[::-1]}")
    is_palindrome = s == s[::-1]
    print(f"The string is a palindrome: {is_palindrome}")
def print_set(lower_bound, upper_bound):
    numbers = {n for n in range(lower_bound + 1, upper_bound) if n % 7 == 0 and n % 5 != 0}
    print(numbers)
if __name__ == "__main__":
    test_string = "11411"
    print_string_properties(test_string)
    lower_bound = 11
    upper_bound = 21
    print_set(lower_bound, upper_bound)