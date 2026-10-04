import re
from collections import Counter
import math
original_document = 'AI is our friend and it has been friendly'
new_document = 'AI and humans have always been friendly'
def document_to_vector(document):
    word_list = re.compile(r'\w+')
    all_words = word_list.findall(document.lower())
    return Counter(all_words)
def cosine_similarity(vector1, vector2):
    common_words = set(vector1.keys()) & set(vector2.keys())
    sum_of_vectors = sum(vector1[word] * vector2[word] for word in common_words)
    sum_of_vec1 = sum(vector1[word]**2 for word in vector1.keys())
    sum_of_vec2 = sum(vector2[word]**2 for word in vector2.keys())
    multiplier_of_sum = math.sqrt(sum_of_vec1) * math.sqrt(sum_of_vec2)
    if multiplier_of_sum == 0:
        return 0.0
    return sum_of_vectors / multiplier_of_sum
def main():
    vector_1 = document_to_vector(original_document)
    vector_2 = document_to_vector(new_document)
    plagiarism_factor = cosine_similarity(vector_1, vector_2)
    print('Plagiarism factor:', plagiarism_factor)
    if plagiarism_factor > 0.40:
        print('Your document is a plagiarism.')
    else:
        print('Your document is not a plagiarism.')
if __name__ == '__main__':
    main()