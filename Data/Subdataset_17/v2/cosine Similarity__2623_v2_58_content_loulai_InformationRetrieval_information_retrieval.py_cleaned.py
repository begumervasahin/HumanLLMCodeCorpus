import re
from stop_list import closed_class_stop_words
def read_queries(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace(r"\s", "")
def get_query_nums(string):
    return [match.replace(".I ", "") for match in re.findall(r"\.I \d{3}", string)]
def get_query_strings(string):
    return [match.strip() for match in re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)]
def trim(string):
    words = re.sub(r"\n|\r", " ", string).split()
    return [word for word in words if word not in closed_class_stop_words]
def get_tf(words):
    return {word: words.count(word) for word in set(words)}
def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    queries = read_queries("cran.qry")
    query_strings = get_query_strings(queries)
    for query in query_strings:
        print(query)
    trimmed_content = trim(open("cran2.qry", 'r').read())
    print(trimmed_content)
    term_frequency = get_tf(trimmed_content)
    print_dict(term_frequency)