import re
def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()
def find_words_of_length(length, text):
    pattern = r'\b\w{' + str(length) + r'}\w*\b'
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
def filter_emails_without_gov(emails):
    return [email for email in emails if not email.endswith('.gov')]
def print_results(phone_numbers, names_and_titles, long_words, emails, filtered_emails):
    print("Number of phone numbers found:", len(phone_numbers))
    print("Number of names and titles found:", len(names_and_titles))
    print("Words with 12 characters or more:", long_words)
    print("Number of emails found:", len(emails))
    print("Number of emails without .gov ending:", len(filtered_emails))
def remember(text, file_path):
    with open(file_path, "a") as file:
        file.write(text + "\n")
if __name__ == "__main__":
    data = read_file("names.txt")
    phone_numbers = find_phone_numbers(data)
    names_and_titles = find_names_and_titles(data)
    long_words = find_words_of_length(12, data)
    emails = find_emails(data)
    filtered_emails = filter_emails_without_gov(emails)
    print_results(phone_numbers, names_and_titles, long_words, emails, filtered_emails)
    memory_text = input("What would you like to remember? ")
    remember(memory_text, "database.txt")