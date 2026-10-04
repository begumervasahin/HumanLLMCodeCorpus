def replace_sep(my_string, sep1, sep2):
    if not my_string:
        return ""
    if my_string.startswith(sep1):
        return sep2 + replace_sep(my_string[len(sep1):], sep1, sep2)
    return my_string[0] + replace_sep(my_string[1:], sep1, sep2)
def count_siblings(number_elves):
    if number_elves <= 0:
        return 0
    if number_elves % 2 == 1:
        return 3 + count_siblings(number_elves - 1)
    return 1 + count_siblings(number_elves - 1)
def extractor(string):
    if not string:
        return ""
    if string[0] != "(":
        return extractor(string[1:])
    if string[-1] != ")":
        return extractor(string[:-1])
    return string
def is_palindrome(sequence):
    sequence = sequence.replace(" ", "")
    if len(sequence) < 2:
        return True
    if sequence[0] != sequence[-1]:
        return False
    return is_palindrome(sequence[1:-1])
def tester():
    print(replace_sep("hope*you*are*enjoying*the*course", "*", " "))
    print(replace_sep("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(replace_sep("popopopopo", "p", "x"))
    print(replace_sep("xxxxx", "o", "b"))
    print(count_siblings(0))
    print(count_siblings(100))
    print(count_siblings(2))
    print(count_siblings(5))
    print(count_siblings(-9))
    print(extractor("(hello world)"))
    print(extractor("My country (of origin) is Canada"))
    print(extractor("I do not have any parenthesis"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("redrumsirismurder"))
def main():
    tester()
if __name__ == "__main__":
    main()