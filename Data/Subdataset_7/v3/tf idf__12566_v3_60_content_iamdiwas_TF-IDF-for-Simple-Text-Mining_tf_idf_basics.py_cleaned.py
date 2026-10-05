import nltk
import math
from nltk.tokenize import word_tokenize
b1 = {
    "text_1": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text1.txt',
    "text_2": 'W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text2.txt'
}
def fonk1(file_path):
    with open(file_path, "rU") as file:
        return file.read()
b2 = {name: fonk1(path) for name, path in b1.items()}
def fonk2(text):
    b3 = word_tokenize(text)
    b4 = nltk.FreqDist(b3)
    return b4
def fonk3(texts, word):
    b5 = sum(word in doc for doc in texts.values())
    b6 = math.log(len(texts) / (1 + b5))
    return b6
def fonk4(texts, text_name):
    b7 = {}
    b8 = fonk2(texts[text_name])
    for term in b8:
        if term.isalpha():
            b6 = fonk3(texts, term)
            b9 = b8[term]
            b7[term] = round(b6 * b9, 3)
    return b7
b10 = "text_1"
b7 = fonk4(b2, b10)
print(f"TF-IDF scores for {b10}:")
print(b7)