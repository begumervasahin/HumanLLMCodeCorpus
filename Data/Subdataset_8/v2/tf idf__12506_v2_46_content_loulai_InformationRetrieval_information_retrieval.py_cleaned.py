import re
from stop_list import closed_class_stop_words
def get_query_nums(string):
    query_nums = []
    matches = re.findall(r".I \d{3}", string)
    for match in matches:
        query_nums.append(match.replace(".I ", ""))
    return query_nums
def get_query_strings(string):
    query_strings = []
    matches = re.findall(r"([a-z ]+\n){1,3}[a-z ]+\.", string)
    for match in matches:
        query_strings.append(match)
    return query_strings
def trim(string):
    trimmed_words = filter(None, re.sub(r"\n|\r", " ", string).split(" "))
    stop_words = closed_class_stop_words
    for stop_word in stop_words:
        while stop_word in trimmed_words:
            trimmed_words.remove(stop_word)
    return trimmed_words
def get_tf(array):
    terms = list(set(array))
    term_frequency = dict.fromkeys(terms, 0)
    for word in array:
        term_frequency[word] += 1
    return term_frequency
def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key, value)
queries = open("cran.qry", 'r').read()
queries.replace("\s ", "")
query_strings = get_query_strings(queries)
for i, query_string in enumerate(query_strings):
    print(f"Query {i+1}:")
    print(trim(query_string))
    print()
print("Term Frequencies:")
example_query = open("cran2.qry", 'r').read()
example_query_terms = trim(example_query)
example_query_tf = get_tf(example_query_terms)
print_dict(example_query_tf)