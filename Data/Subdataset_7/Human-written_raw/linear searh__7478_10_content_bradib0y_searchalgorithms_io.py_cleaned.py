import re
b1 = open("names.txt", encoding="utf-8")
b2 = b1.read()
b1.close()
b3 = r'something'
print(re.match(r'Love', b2))
print(re.search(r'Chalkley', b2))
b4 = re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', b2)
print("There are this many phone numbers:", len(b4))
b5 = re.findall(r'\w*, \w*', b2)
print("There are this many names and titles:", len(b5))
def fonk1(c, s):
    b3 = r'\w{'
    b3 += str(c)
    b3 += r'}\w*'
    return re.findall(b3, s)
print(fonk1(12, b2))
b6 = re.findall(r'[\w\d\-\+\.]+@[\w\d\-\+\.]+', b2)
print("There are this many b6:", len(b6))
b7 = re.findall(r'[\w\d\-\+\.]+@[\w\d\-\+\.]+', b2)
print("There are this many b6 without .gov ending:", len(b6))
print(re.findall(r'''
^([-\w ]+,\s[-\w ]+)\t
([-\w\d.+]+@[-\w\d.]+)\t
(\(?\d{3}\)?-?\s?\d{3}-\d{4})\t
([\w\s]+,\s[\w\s]+)\t
(@[\w\d]+)$
''', b2, re.X))
def fonk2(thing):
    b8 = open("database.txt", "a")
    b8.write(thing + "\n")
    b8.close()
fonk2(input("What should I remember?"))