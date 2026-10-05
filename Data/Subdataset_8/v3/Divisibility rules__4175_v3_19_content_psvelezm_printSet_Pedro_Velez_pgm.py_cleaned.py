def print_string_properties(input_string):
    char_list = list(input_string)
    even_char_list = [char for index, char in enumerate(char_list) if index % 2 == 0]
    even_string = "".join(even_char_list)
    print(f"The input string is: {input_string}")
    print(f"The characters that have even indexes are: {even_string}")
    print(f"The string in reverse order is: {input_string[::-1]}")
    if input_string == input_string[::-1]:
        print("The string is a palindrome: True")
    else:
        print("The string is a palindrome: False")
def print_set(start, end):
    num_list = []
    for i in range(start + 1, end):
        if i % 7 == 0 and i % 5 != 0:
            num_list.append(i)
    result_set = set(num_list)
    print(result_set)
print_string_properties("11411")
print_set(11, 21)