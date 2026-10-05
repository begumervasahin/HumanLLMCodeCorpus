import re
with open("names.txt", encoding="utf-8") as names_file:
    data = names_file.read()
def find_words_of_length(length, text):
    pattern = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(pattern, text)
phones = re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data)
names_and_titles = re.findall(r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b', data)
emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)
emails_without_gov = [email for email in emails if not email.endswith('.gov')]
print("Number of phone numbers found:", len(phones))
print("Number of names and titles found:", len(names_and_titles))
print("Words with 12 characters or more:", find_words_of_length(12, data))
print("Number of emails found:", len(emails))
print("Number of emails without .gov ending:", len(emails_without_gov))
def remember(thing):
    with open("database.txt", "a") as file:
        file.write(thing + "\n")
thing_to_remember = input("What would you like to remember? ")
remember(thing_to_remember)