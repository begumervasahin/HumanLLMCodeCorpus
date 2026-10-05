import re
def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()
def find_words_of_length(length, text):
    pattern = r'\b\w{' + str(length) + r'}\w*\b'
    return re.findall(pattern, text)
def find_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', text)
def find_names_and_titles(text):
    return re.findall(r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b', text)
def find_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)
def find_emails_without_gov(emails):
    return [email for email in emails if not email.endswith('.gov')]
def print_results(phones, names_and_titles, words, emails, emails_without_gov):
    print("Number of phone numbers found:", len(phones))
    print("Number of names and titles found:", len(names_and_titles))
    print("Words with 12 characters or more:", words)
    print("Number of emails found:", len(emails))
    print("Number of emails without .gov ending:", len(emails_without_gov))
def remember(thing, file_path):
    with open(file_path, "a") as file:
        file.write(thing + "\n")
if __name__ == "__main__":
    data = read_file("names.txt")
    phones = find_phone_numbers(data)
    names_and_titles = find_names_and_titles(data)
    words = find_words_of_length(12, data)
    emails = find_emails(data)
    emails_without_gov = find_emails_without_gov(emails)
    print_results(phones, names_and_titles, words, emails, emails_without_gov)
    thing_to_remember = input("What would you like to remember? ")
    remember(thing_to_remember, "database.txt")