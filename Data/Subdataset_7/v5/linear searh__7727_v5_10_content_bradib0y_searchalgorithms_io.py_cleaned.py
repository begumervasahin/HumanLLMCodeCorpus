import re
def fonk1(filename):
    with open(filename, b1 = "utf-8") as file:
        return file.read()
def fonk2(b2, b4):
    return re.match(b2, b4)
def fonk3(b2, b4):
    return re.search(b2, b4)
def fonk4(b4):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', b4)
def fonk5(b4):
    return re.findall(r'\w*, \w*', b4)
def fonk6(length, string):
    b2 = r'\b\w{' + str(length) + r'}\b'
    return re.findall(b2, string)
def fonk7(b4):
    return re.findall(r'[\w\d\-\+\.]+@[\w\d\-\+\.]+', b4)
def fonk8(b4):
    return [email for email in fonk7(b4) if not email.endswith('.gov')]
def fonk9(b4):
    return re.findall(r'''
    ([-\w ]+,\s[-\w ]+)\t
    ([-\w\d.+]+@[-\w\d.]+)\t
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t
    ([\w\s]+,\s[\w\s]+)\t
    (@[\w\d]+)
    ''', b4, re.X)
def fonk10(thing):
    with open("database.txt", "a") as file:
        file.write(thing + "\n")
if b3 = = "__main__":
    b4 = fonk1("names.txt")
    print(fonk2(r'Love', b4))
    print(fonk3(r'Chalkley', b4))
    b5 = fonk4(b4)
    print("There are this many phone numbers:", len(b5))
    b6 = fonk5(b4)
    print("There are this many names and titles:", len(b6))
    print(fonk6(12, b4))
    b7 = fonk7(b4)
    print("There are this many b7:", len(b7))
    b8 = fonk8(b4)
    print("There are this many b7 without .gov ending:", len(b8))
    print(fonk9(b4))
    fonk10(input("What should I remember?"))