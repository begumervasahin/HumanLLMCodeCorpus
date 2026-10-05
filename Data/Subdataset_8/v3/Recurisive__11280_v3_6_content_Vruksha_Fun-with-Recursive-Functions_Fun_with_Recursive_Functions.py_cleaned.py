def replace_separator(string, old_sep, new_sep):
    if not string:
        return ""
    elif string.startswith(old_sep):
        return new_sep + replace_separator(string[len(old_sep):], old_sep, new_sep)
    else:
        return string[0] + replace_separator(string[1:], old_sep, new_sep)
def count_siblings(number_of_elves):
    if number_of_elves == 0:
        return 0
    if number_of_elves % 2 == 1:
        return 3 + count_siblings(number_of_elves - 1)
    if number_of_elves % 2 == 0:
        return 1 + count_siblings(number_of_elves - 1)
def extract_innermost_parentheses(expression):
    if not expression:
        return ""
    elif expression[0] != "(":
        return extract_innermost_parentheses(expression[1:])
    elif expression[-1] != ")":
        new_expression = expression[:-1]
        return extract_innermost_parentheses(new_expression)
    else:
        return expression
def is_palindrome(string):
    string = ''.join(string.split())
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])
def run_tests():
    print(replace_separator("hope*you*are*enjoying*the*course", "*", " "))
    print(replace_separator("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(replace_separator("popopopopo", "p", "x"))
    print(replace_separator("xxxxx", "o", "b"))
    print(count_siblings(0))
    print(count_siblings(100))
    print(count_siblings(2))
    print(count_siblings(5))
    print(count_siblings(-9))
    print(extract_innermost_parentheses("(hello world)"))
    print(extract_innermost_parentheses("My country (of origin) is Canada"))
    print(extract_innermost_parentheses("I do not have any parenthesis"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("redrumsirismurder"))
if __name__ == "__main__":
    run_tests()