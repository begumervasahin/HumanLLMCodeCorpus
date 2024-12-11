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
def fonk2(doc, text):
    b3 = word_tokenize(doc[text])
    b4 = nltk.FreqDist(b3)
    return b4
def fonk3(doc, word):
    b5 = [word in doc[file] for file in doc]
    b6 = math.log(len(b5) / sum(b5))
    return b6
def fonk4(doc, text):
    b7 = {}
    b8 = fonk2(doc, text)
    for term in b8:
        if term.isalpha():
            b6 = fonk3(doc, term)
            b9 = b8[term]
            b10 = b6 * b9
            b7[term] = round(b10, 3)
    return b7
b11 = "text_1"
b7 = fonk4(b2, b11)
print(f"TF-IDF scores for {b11}:")
print(b7)