'''The following function is responsible for taking a string and two characters as the input
and returning a new string with sep2 replacing sep1. '''
def replaceSep(myString,sep1,sep2):
    if not myString:
        return ""
    elif myString [:len(sep1)] == sep1:
        return sep2 + replaceSep(myString[len(sep1):], sep1, sep2)
    else:
        return myString[0] + replaceSep(myString[1:], sep1, sep2)
'''The following function will return the number of siblings that the eleves have in total. Odd numbered elves
have three siblings and even numbered elves have 1 sibling.'''
def countSiblings(numberElves):
    if numberElves == 0:
        return 0
    if numberElves % 2 == 1:
        return 3 + countSiblings(numberElves - 1)
    if numberElves % 2 == 0:
        return 1 + countSiblings(numberElves - 1)
'''The following function will take a string and print the sub string enclosed within brackets.'''
def extractor(string):
    if string [:1] != "(":
        return extractor(string[1:])
    elif string[len(string)-1:] != ")":
        newString = string[:string[len(string)-1]]
        return extractor(newString)
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
'''This is the tester code for the functions written above.'''
def tester():
   print(replaceSep("hope*you*are*enjoying*the*course", "*", " "))
   print(replaceSep("Hi.  I am having fun.  Are you?", ".", "!!"))
   print(replaceSep("popopopopo", "p", "x"))
   print(replaceSep("xxxxx", "o", "b"))
   print(countSiblings(0))
   print(countSiblings(100))
   print(countSiblings(2))
   print(countSiblings(5))
   print(countSiblings(-9))
   print(extractor("(hello world)"))
   print(extractor("My country (of origin) is Canada"))
   print(extractor("I do not have any parenthesis"))
   print(palindrome("racecar"))
   print(palindrome("hello"))
   print(palindrome("redrumsirismurder"))
def main():
    tester()
    replaceSep(myString,sep1,sep2)
    countSiblings(numberElves)
    extractor(string)
    palindrome(sequence)