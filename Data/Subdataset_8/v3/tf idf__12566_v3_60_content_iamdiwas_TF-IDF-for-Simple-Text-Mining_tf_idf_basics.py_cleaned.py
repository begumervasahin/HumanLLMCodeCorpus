import nltk
import math
from nltk.tokenize import word_tokenize
TEXT_PATHS = {
    "text_1": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text1.txt',
    "text_2": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text2.txt'
}
def read_text(file_path):
    with open(file_path, "rU") as file:
        return file.read()
TEXTS = {name: read_text(path) for name, path in TEXT_PATHS.items()}
def calculate_term_frequency(text):
    word_tokens = word_tokenize(text)
    words_freq = nltk.FreqDist(word_tokens)
    return words_freq
def calculate_inverse_document_frequency(texts, word):
    word_count = sum(word in doc for doc in texts.values())
    idf = math.log(len(texts) / (1 + word_count))
    return idf
def calculate_tf_idf(texts, text_name):
    tfidf_scores = {}
    term_frequency = calculate_term_frequency(texts[text_name])
    for term in term_frequency:
        if term.isalpha():
            idf = calculate_inverse_document_frequency(texts, term)
            tf_term = term_frequency[term]
            tfidf_scores[term] = round(idf * tf_term, 3)
    return tfidf_scores
selected_text = "text_1"
tfidf_scores = calculate_tf_idf(TEXTS, selected_text)
print(f"TF-IDF scores for {selected_text}:")
print(tfidf_scores)