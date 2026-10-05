import re
with open("names.txt", encoding="utf-8") as names_file:
    data = names_file.read()
def find_words(length, text):
    pattern = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(pattern, text)
phones = re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data)
namesAndTitles = re.findall(r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b', data)
emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)
emailsWithoutGov = [email for email in emails if not email.endswith('.gov')]
print("There are this many phone numbers:", len(phones))
print("There are this many names and titles:", len(namesAndTitles))
print("Words with 12 characters or more:", find_words(12, data))
print("There are this many emails:", len(emails))
print("There are this many emails without .gov ending:", len(emailsWithoutGov))
def remember(thing):
    with open("database.txt", "a") as file:
        file.write(thing + "\n")
thing_to_remember = input("What should I remember? ")
remember(thing_to_remember)