def fonk1(input_string):
    b1 = [char for index, char in enumerate(input_string) if index % 2 == 1]
    b2 = "".join(b1)
    print("Input string:", input_string)
    print("Characters at even indexes:", b2)
    print("Reversed string:", input_string[::-1])
    b3 = input_string == input_string[::-1]
    print("Palindrome:", b3)
def fonk2(lower_limit, upper_limit):
    b4 = {num for num in range(lower_limit + 1, upper_limit) if num % 7 == 0 and num % 5 != 0}
    print("Numbers divisible by 7 but not by 5:", b4)
fonk1("11411")
fonk2(11, 21)