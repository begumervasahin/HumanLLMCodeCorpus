'''The following function is responsible for taking a string and two characters as the input
and returning a new string with sep2 replacing sep1. '''
def fonk1(myString,sep1,sep2):
    if not myString:
        return ""
    elif myString [:len(sep1)] == sep1:
        return sep2 + fonk1(myString[len(sep1):], sep1, sep2)
    else:
        return myString[0] + fonk1(myString[1:], sep1, sep2)
'''The following function will return the number of siblings that the eleves have in total. Odd numbered elves
have three siblings and even numbered elves have 1 sibling.'''
def fonk2(b1):
    if b1 = = 0:
        return 0
    if b1 % b2 = = 1:
        return 3 + fonk2(b1 - 1)
    if b1 % b2 = = 0:
        return 1 + fonk2(b1 - 1)
'''The following function will take a string and print the sub string enclosed within brackets.'''
def fonk3(string):
    if string [:1] != "(":
        return fonk3(string[1:])
    elif string[len(string)-1:] != ")":
        b3 = string[:string[len(string)-1]]
        return fonk3(b3)
    else:
        return string
def fonk4(b4):
    b4 = b4.split()
    b4 = ''.join(b4)
    if len(b4) < b2:
        return True
    if b4[0] != b4[-1]:
            return False
    return fonk4(b4[1:-1])
'''This is the tester code for the functions written above.'''
def fonk5():
   print(fonk1("hope*you*are*enjoying*the*course", "*", " "))
   print(fonk1("Hi.  I am having fun.  Are you?", ".", "!!"))
   print(fonk1("popopopopo", "p", "x"))
   print(fonk1("xxxxx", "o", "b"))
   print(fonk2(0))
   print(fonk2(100))
   print(fonk2(b2))
   print(fonk2(5))
   print(fonk2(-9))
   print(fonk3("(hello world)"))
   print(fonk3("My country (of origin) is Canada"))
   print(fonk3("I do not have any parenthesis"))
   print(fonk4("racecar"))
   print(fonk4("hello"))
   print(fonk4("redrumsirismurder"))
def fonk6():
    fonk5()
    fonk1(myString,sep1,sep2)
    fonk2(b1)
    fonk3(string)
    fonk4(b4)