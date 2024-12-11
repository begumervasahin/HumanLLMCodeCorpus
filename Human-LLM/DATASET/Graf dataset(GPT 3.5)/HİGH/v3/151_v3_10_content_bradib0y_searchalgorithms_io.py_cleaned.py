import re
def fonk1(file_path):
    with open(file_path, b1 = "utf-8") as file:
        return file.read()
def fonk2(length, text):
    b2 = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(b2, text)
def fonk3(text):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', text)
def fonk4(text):
    return re.findall(r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b', text)
def fonk5(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)
def fonk6(b8):
    return [email for email in b8 if not email.endswith('.gov')]
def fonk7(b5, b6, b7, b8, b9):
    print("Number of phone numbers found:", len(b5))
    print("Number of names and titles found:", len(b6))
    print("Words with 12 characters or more:", b7)
    print("Number of b8 found:", len(b8))
    print("Number of b8 without .gov ending:", len(b9))
def fonk8(thing, file_path):
    with open(file_path, "a") as file:
        file.write(thing + "\n")
if b3 = = "__main__":
    b4 = fonk1("names.txt")
    b5 = fonk3(b4)
    b6 = fonk4(b4)
    b7 = fonk2(12, b4)
    b8 = fonk5(b4)
    b9 = fonk6(b8)
    fonk7(b5, b6, b7, b8, b9)
    b10 = input("What would you like to remember? ")
    fonk8(b10, "database.txt")