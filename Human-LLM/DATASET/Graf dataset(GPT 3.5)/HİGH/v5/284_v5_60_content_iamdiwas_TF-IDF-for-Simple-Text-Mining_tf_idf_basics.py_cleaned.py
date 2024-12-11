import nltk
import math
from nltk.tokenize import word_tokenize
b1 = {
    "text_1": open('W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text1.txt', "rU").read(),
    "text_2": open('W:/Diwas/Python_projects/NLP_Codes/tf_idf_data/text2.txt', "rU").read(),
}
def fonk1(doc, text):
    b2 = word_tokenize(doc[text])
    b3 = nltk.FreqDist(b2)
    return b3
def fonk2(doc, word):
    b4 = [word in doc[file] for file in doc]
    b5 = math.log(len(b4) / sum(b4))
    return b5
def fonk3(doc, text):
    b6 = {}
    b7 = fonk1(doc, text)
    for term in b7:
        if term.isalpha():
            b5 = fonk2(doc, term)
            b8 = fonk1(doc, text)[term]
            b9 = b5 * b8
            b6[term] = round(b9, 3)
    return b6