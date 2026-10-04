import re
def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()
def find_words_of_length(text, length):
    pattern = rf'\b\w{{{length}}}\w*\b'
    return re.findall(pattern, text)
def find_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}'
    return re.findall(phone_pattern, text)
def find_names_and_titles(text):
    name_title_pattern = r'\b[A-Z][a-z]*,\s[A-Z][a-z]*\b'
    return re.findall(name_title_pattern, text)
def find_emails(text):
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    return re.findall(email_pattern, text)
def filter_out_gov_emails(emails):
    return [email for email in emails if not email.endswith('.gov')]
def print_results(phone_numbers, names_and_titles, long_words, emails, non_gov_emails):
    print("Number of phone numbers found:", len(phone_numbers))
    print("Number of names and titles found:", len(names_and_titles))
    print("Words with 12 characters or more:", long_words)
    print("Number of emails found:", len(emails))
    print("Number of emails without .gov ending:", len(non_gov_emails))
def remember(thing, file_path):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(thing + "\n")
if __name__ == "__main__":
    file_content = read_file("names.txt")
    phone_numbers = find_phone_numbers(file_content)
    names_and_titles = find_names_and_titles(file_content)
    long_words = find_words_of_length(file_content, 12)
    emails = find_emails(file_content)
    non_gov_emails = filter_out_gov_emails(emails)
    print_results(phone_numbers, names_and_titles, long_words, emails, non_gov_emails)
    thing_to_remember = input("What would you like to remember? ")
    remember(thing_to_remember, "database.txt")