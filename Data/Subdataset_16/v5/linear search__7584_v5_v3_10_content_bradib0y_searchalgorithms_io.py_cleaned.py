import re
def fonk1(file_path):
    with open(file_path, b1 = "utf-8") as file:
        return file.read()
def fonk2(length, text):
    b2 = fr'\b\w{{{length}}}\w*\b'
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
def fonk6(b10):
    return [email for email in b10 if not email.endswith('.gov')]
def fonk7(b7, b8, b9, b10, b11):
    print("Number of phone numbers found:", len(b7))
    print("Number of names and titles found:", len(b8))
    print("Words with 12 characters or more:", b9)
    print("Number of b10 found:", len(b10))
    print("Number of b10 without .gov ending:", len(b11))
def fonk8(text, file_path):
    with open(file_path, "a") as file:
        file.write(text + "\n")
def fonk9():
    b6 = fonk1("names.txt")
    b7 = fonk3(b6)
    b8 = fonk4(b6)
    b9 = fonk2(12, b6)
    b10 = fonk5(b6)
    b11 = fonk6(b10)
    fonk7(b7, b8, b9, b10, b11)
    b12 = input("What would you like to remember? ")
    fonk8(b12, "database.txt")
if b13 = = "__main__":
    fonk9()