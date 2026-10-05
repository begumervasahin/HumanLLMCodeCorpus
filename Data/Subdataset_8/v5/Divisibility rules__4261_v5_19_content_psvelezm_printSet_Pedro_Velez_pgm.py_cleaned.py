def print_string_properties(input_string):
    characters_with_even_indexes = [char for index, char in enumerate(input_string) if index % 2 == 1]
    even_string = "".join(characters_with_even_indexes)
    print("Input string:", input_string)
    print("Characters at even indexes:", even_string)
    print("Reversed string:", input_string[::-1])
    is_palindrome = input_string == input_string[::-1]
    print("Palindrome:", is_palindrome)
def print_set(lower_limit, upper_limit):
    numbers = {num for num in range(lower_limit + 1, upper_limit) if num % 7 == 0 and num % 5 != 0}
    print("Numbers divisible by 7 but not by 5:", numbers)
print_string_properties("11411")
print_set(11, 21)