import re
import math
def cosine_similarity(input_query, database_text):
    try:
        universal_set_of_unique_words = []
        match_percentage = 0
        lowercase_query = input_query.lower()
        query_word_list = re.sub("[^\w]", " ", lowercase_query).split()
        for word in query_word_list:
            if word not in universal_set_of_unique_words:
                universal_set_of_unique_words.append(word)
        database_word_list = re.sub("[^\w]", " ", database_text.lower()).split()
        for word in database_word_list:
            if word not in universal_set_of_unique_words:
                universal_set_of_unique_words.append(word)
        query_term_frequencies = [query_word_list.count(word) for word in universal_set_of_unique_words]
        database_term_frequencies = [database_word_list.count(word) for word in universal_set_of_unique_words]
        dot_product_tf = sum(query_term_frequencies[i] * database_term_frequencies[i] for i in range(len(query_term_frequencies)))
        query_vector_magnitude = math.sqrt(sum(tf ** 2 for tf in query_term_frequencies))
        database_vector_magnitude = math.sqrt(sum(tf ** 2 for tf in database_term_frequencies))
        match_percentage = (dot_product_tf / (query_vector_magnitude * database_vector_magnitude)) * 100
        result_output = f"Input query text matches {match_percentage:.02f}% with database."
        return result_output
    except Exception as e:
        return "Please Enter Valid Data"
input_query = "Enter your query here."
database_text = open("database1.txt", "r").read()
result = cosine_similarity(input_query, database_text)
print(result)