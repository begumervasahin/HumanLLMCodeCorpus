import re
with open("names.txt", b1 = "utf-8") as names_file:
    b2 = names_file.read()
def fonk1(length, text):
    b3 = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(b3, text)
b4 = re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', b2)
b5 = re.findall(r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b', b2)
b6 = re.findall(r'[\w\.-]+@[\w\.-]+', b2)
b7 = [email for email in b6 if not email.endswith('.gov')]
print("Number of phone numbers found:", len(b4))
print("Number of names and titles found:", len(b5))
print("Words with 12 characters or more:", fonk1(12, b2))
print("Number of b6 found:", len(b6))
print("Number of b6 without .gov ending:", len(b7))
def fonk2(thing):
    with open("database.txt", "a") as file:
        file.write(thing + "\n")
b8 = input("What would you like to remember? ")
fonk2(b8)