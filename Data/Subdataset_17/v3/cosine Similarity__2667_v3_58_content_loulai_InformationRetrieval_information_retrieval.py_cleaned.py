import re
from stop_list import closed_class_stop_words
def read_queries(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace(r"\s", "")
def get_query_nums(content):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", content)]
def get_query_strings(content):
    return [match.strip() for match in re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", content)]
def trim(text):
    words = re.sub(r"\n|\r", " ", text).split()
    return [word for word in words if word not in closed_class_stop_words]
def get_term_frequency(words):
    return {word: words.count(word) for word in set(words)}
def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def main():
    queries = read_queries("cran.qry")
    query_strings = get_query_strings(queries)
    print("Extracted Query Strings:")
    for query in query_strings:
        print(query)
    with open("cran2.qry", 'r') as file:
        cran2_content = file.read()
    trimmed_content = trim(cran2_content)
    print("\nTrimmed Content:")
    print(trimmed_content)
    term_frequency = get_term_frequency(trimmed_content)
    print("\nTerm Frequencies:")
    print_dictionary(term_frequency)
if __name__ == "__main__":
    main()