import re
from stop_list import closed_class_stop_words
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
def remove_whitespaces(text):
    return text.replace("\s ", "")
def extract_query_numbers(text):
    return re.findall(r".I \d{3}", text)
def extract_query_strings(text):
    return re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", text)
def trim_query_string(string):
    words = re.split(r"\s+|\n+|\r+", string)
    trimmed_words = [word for word in words if word not in closed_class_stop_words]
    return trimmed_words
def calculate_term_frequency(words):
    term_frequency = {}
    for word in words:
        term_frequency[word] = term_frequency.get(word, 0) + 1
    return term_frequency
def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key, value)
if __name__ == "__main__":
    queries = read_file("cran.qry")
    queries = remove_whitespaces(queries)
    query_strings = extract_query_strings(queries)
    print(query_strings)
    trimmed_words = trim_query_string(read_file("cran2.qry"))
    print(trimmed_words)