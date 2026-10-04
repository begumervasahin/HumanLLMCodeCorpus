import re
from stop_list import closed_class_stop_words
queries = open("cran.qry", 'r').read()
queries = queries.replace("\s", "")
def get_query_nums(string):
    query_nums = []
    matches = re.findall(r"\.I \d{3}", string)
    for match in matches:
        query_nums.append(match.replace(".I ", ""))
    return query_nums
def get_query_strings(string):
    query_strings = []
    matches = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
    for match in matches:
        query_strings.append(match.strip())
    return query_strings
def trim(string):
    words = re.sub(r"\n|\r", " ", string).split()
    trimmed_words = [word for word in words if word not in closed_class_stop_words]
    return trimmed_words
def get_tf(array):
    terms = list(set(array))
    term_frequency = {term: array.count(term) for term in terms}
    return term_frequency
def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    query_strings = get_query_strings(queries)
    for query in query_strings:
        print(query)
    trimmed_content = trim(open("cran2.qry", 'r').read())
    print(trimmed_content)
    term_frequency = get_tf(trimmed_content)
    print_dict(term_frequency)