def print_string_properties(S):
    char_list = list(S)
    even_char_list = [char for index, char in enumerate(char_list) if index % 2 == 0]
    even_string = "".join(even_char_list)
    print("The input string is:", S)
    print("The characters that have even indexes are:", even_string)
    print("The string in reverse order is:", S[::-1])
    if S == S[::-1]:
        print("The string is a palindrome: True")
    else:
        print("The string is a palindrome: False")
def print_set(L, H):
    num_list = []
    for i in range(L + 1, H):
        if i % 7 == 0 and i % 5 != 0:
            num_list.append(i)
    M = set(num_list)
    print(M)
print_string_properties("11411")
print_set(11, 21)