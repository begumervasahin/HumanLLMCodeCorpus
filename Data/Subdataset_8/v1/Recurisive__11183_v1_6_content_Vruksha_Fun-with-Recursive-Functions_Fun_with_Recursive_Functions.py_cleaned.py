def replace_sep(my_string, sep1, sep2):
    if not my_string:
        return ""
    elif my_string[:len(sep1)] == sep1:
        return sep2 + replace_sep(my_string[len(sep1):], sep1, sep2)
    else:
        return my_string[0] + replace_sep(my_string[1:], sep1, sep2)
def count_siblings(number_elves):
    if number_elves == 0:
        return 0
    if number_elves % 2 == 1:
        return 3 + count_siblings(number_elves - 1)
    if number_elves % 2 == 0:
        return 1 + count_siblings(number_elves - 1)
def extractor(string):
    if string[:1] != "(":
        return extractor(string[1:])
    elif string[len(string) - 1:] != ")":
        new_string = string[:string[len(string) - 1]]
        return extractor(new_string)
    else:
        return string
def palindrome(sequence):
    sequence = sequence.split()
    sequence = ''.join(sequence)
    if len(sequence) < 2:
        return True
    if sequence[0] != sequence[-1]:
            return False
    return palindrome(sequence[1:-1])
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
    print(palindrome("racecar"))
    print(palindrome("hello"))
    print(palindrome("redrumsirismurder"))
if __name__ == "__main__":
    tester()