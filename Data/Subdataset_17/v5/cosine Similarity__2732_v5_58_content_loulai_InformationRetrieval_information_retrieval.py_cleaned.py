import re
from stop_list import closed_class_stop_words
def read_queries(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.replace(r"\s ", "")
def get_query_numbers(content):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", content)]
def get_query_texts(content):
    matches = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", content)
    return [match.strip() for match in matches]
def trim_text(text):
    words = re.sub(r"\n|\r", " ", text).split()
    return [word for word in words if word not in closed_class_stop_words]
def calculate_term_frequency(words):
    term_frequency = {word: words.count(word) for word in set(words)}
    return term_frequency
def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def main():
    queries = read_queries("cran.qry")
    query_numbers = get_query_numbers(queries)
    print("Query Numbers:")
    print(query_numbers)
    query_texts = get_query_texts(queries)
    print("\nExtracted Query Strings:")
    for query in query_texts:
        print(query)
    with open("cran2.qry", 'r') as file:
        cran2_content = file.read()
    trimmed_content = trim_text(cran2_content)
    print("\nTrimmed Content:")
    print(trimmed_content)
    term_frequency = calculate_term_frequency(trimmed_content)
    print("\nTerm Frequencies:")
    print_dictionary(term_frequency)
if __name__ == "__main__":
    main()