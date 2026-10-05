import re
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()
def match_string_start(pattern, data):
    return re.match(pattern, data)
def search_string(pattern, data):
    return re.search(pattern, data)
def find_phone_numbers(data):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data)
def find_names_and_titles(data):
    return re.findall(r'\w*, \w*', data)
def find_words_of_length(length, string):
    pattern = r'\b\w{' + str(length) + r'}\b'
    return re.findall(pattern, string)
def find_emails(data):
    return re.findall(r'[\w\d\-\+\.]+@[\w\d\-\+\.]+', data)
def find_emails_without_gov(data):
    return [email for email in find_emails(data) if not email.endswith('.gov')]
def extract_structured_data(data):
    return re.findall(r'''
    ([-\w ]+,\s[-\w ]+)\t
    ([-\w\d.+]+@[-\w\d.]+)\t
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t
    ([\w\s]+,\s[\w\s]+)\t
    (@[\w\d]+)
    ''', data, re.X)
def remember(thing):
    with open("database.txt", "a") as file:
        file.write(thing + "\n")
if __name__ == "__main__":
    data = read_file("names.txt")
    print(match_string_start(r'Love', data))
    print(search_string(r'Chalkley', data))
    phones = find_phone_numbers(data)
    print("There are this many phone numbers:", len(phones))
    names_and_titles = find_names_and_titles(data)
    print("There are this many names and titles:", len(names_and_titles))
    print(find_words_of_length(12, data))
    emails = find_emails(data)
    print("There are this many emails:", len(emails))
    emails_without_gov = find_emails_without_gov(data)
    print("There are this many emails without .gov ending:", len(emails_without_gov))
    print(extract_structured_data(data))
    remember(input("What should I remember?"))