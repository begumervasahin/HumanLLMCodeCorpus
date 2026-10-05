import nltk
import math
from nltk.tokenize import word_tokenize
text_paths = {
    "text_1": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text1.txt',
    "text_2": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text2.txt'
}
def read_text(file_path):
    with open(file_path, "rU") as file:
        return file.read()
texts = {name: read_text(path) for name, path in text_paths.items()}
def calculate_term_frequency(doc, text):
    word_tokens = word_tokenize(doc[text])
    words_freq = nltk.FreqDist(word_tokens)
    return words_freq
def calculate_inverse_document_frequency(doc, word):
    word_cnt = [word in doc[file] for file in doc]
    idf = math.log(len(word_cnt) / sum(word_cnt))
    return idf
def calculate_tf_idf(doc, text):
    tfidf_scores = {}
    term_frequency = calculate_term_frequency(doc, text)
    for term in term_frequency:
        if term.isalpha():
            idf = calculate_inverse_document_frequency(doc, term)
            tf_term = term_frequency[term]
            tf_idf = idf * tf_term
            tfidf_scores[term] = round(tf_idf, 3)
    return tfidf_scores
selected_text = "text_1"
tfidf_scores = calculate_tf_idf(texts, selected_text)
print(f"TF-IDF scores for {selected_text}:")
print(tfidf_scores)