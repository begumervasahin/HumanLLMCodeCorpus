import nltk
import math
from nltk.tokenize import word_tokenize
dec_texts = {
    "text_1": open('W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text1.txt', "rU").read(),
    "text_2": open('W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text2.txt', "rU").read(),
}
def calculate_term_frequency(doc, text):
    word_tokens = word_tokenize(doc[text])
    word_freq = nltk.FreqDist(word_tokens)
    return word_freq
def calculate_inverse_document_frequency(doc, word):
    word_presence = [word in doc[file] for file in doc]
    idf = math.log(len(word_presence) / sum(word_presence))
    return idf
def calculate_tf_idf(doc, text):
    tfidf_scores = {}
    term_freq = calculate_term_frequency(doc, text)
    for term in term_freq:
        if term.isalpha():
            idf = calculate_inverse_document_frequency(doc, term)
            tf_term = calculate_term_frequency(doc, text)[term]
            tf_idf_score = idf * tf_term
            tfidf_scores[term] = round(tf_idf_score, 3)
    return tfidf_scores