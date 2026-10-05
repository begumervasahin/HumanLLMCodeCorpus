def replace_separator(my_string, sep1, sep2):
    if not my_string:
        return ""
    elif my_string.startswith(sep1):
        return sep2 + replace_separator(my_string[len(sep1):], sep1, sep2)
    else:
        return my_string[0] + replace_separator(my_string[1:], sep1, sep2)
def count_siblings(number_elves):
    if number_elves == 0:
        return 0
    elif number_elves % 2 == 1:
        return 3 + count_siblings(number_elves - 1)
    elif number_elves % 2 == 0:
        return 1 + count_siblings(number_elves - 1)
def extract_substring(string):
    if string[0] != "(":
        return extract_substring(string[1:])
    elif string[-1] != ")":
        return extract_substring(string[:-1])
    else:
        return string
def is_palindrome(sequence):
    sequence = sequence.replace(" ", "")
    if len(sequence) < 2:
        return True
    if sequence[0] != sequence[-1]:
        return False
    return is_palindrome(sequence[1:-1])
def tester():
    print(replace_separator("hope*you*are*enjoying*the*course", "*", " "))
    print(replace_separator("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(replace_separator("popopopopo", "p", "x"))
    print(replace_separator("xxxxx", "o", "b"))
    print(count_siblings(0))
    print(count_siblings(100))
    print(count_siblings(2))
    print(count_siblings(5))
    print(count_siblings(-9))
    print(extract_substring("(hello world)"))
    print(extract_substring("My country (of origin) is Canada"))
    print(extract_substring("I do not have any parenthesis"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("redrumsirismurder"))
def main():
    tester()
if __name__ == "__main__":
    main()