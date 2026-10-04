import re
from collections import Counter
import math
original_document = 'AI is our friend and it has been friendly'
new_document = 'AI and humans have always been friendly'
def document_to_vector(document):
    words = re.findall(r'\w+', document.lower())
    return Counter(words)
def cosine_similarity(vector1, vector2):
    common_words = set(vector1.keys()) & set(vector2.keys())
    numerator = sum(vector1[word] * vector2[word] for word in common_words)
    sum1 = sum(vector1[word]**2 for word in vector1.keys())
    sum2 = sum(vector2[word]**2 for word in vector2.keys())
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if denominator == 0:
        return 0.0
    return numerator / denominator
def main():
    vector_1 = document_to_vector(original_document)
    vector_2 = document_to_vector(new_document)
    plagiarism_factor = cosine_similarity(vector_1, vector_2)
    print(f'Plagiarism factor: {plagiarism_factor:.2f}')
    if plagiarism_factor > 0.40:
        print('Your document is a plagiarism.')
    else:
        print('Your document is not a plagiarism.')
if __name__ == '__main__':
    main()