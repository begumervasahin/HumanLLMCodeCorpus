import re
def fonk1(file_path):
    with open(file_path, b1 = "utf-8") as file:
        return file.read()
def fonk2(length, text):
    b2 = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(b2, text)
def fonk3(text):
    b3 = r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}'
    return re.findall(b3, text)
def fonk4(text):
    b4 = r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b'
    return re.findall(b4, text)
def fonk5(text):
    b5 = r'[\w\.-]+@[\w\.-]+'
    return re.findall(b5, text)
def fonk6(b11):
    return [email for email in b11 if not email.endswith('.gov')]
def fonk7(b8, b9, b10, b11, b12):
    print("Number of phone numbers found:", len(b8))
    print("Number of names and titles found:", len(b9))
    print("Words with 12 characters or more:", b10)
    print("Number of b11 found:", len(b11))
    print("Number of b11 without .gov ending:", len(b12))
def fonk8(text, file_path):
    with open(file_path, "a") as file:
        file.write(text + "\n")
if b6 = = "__main__":
    b7 = fonk1("names.txt")
    b8 = fonk3(b7)
    b9 = fonk4(b7)
    b10 = fonk2(12, b7)
    b11 = fonk5(b7)
    b12 = fonk6(b11)
    fonk7(b8, b9, b10, b11, b12)
    b13 = input("What would you like to remember? ")
    fonk8(b13, "database.txt")