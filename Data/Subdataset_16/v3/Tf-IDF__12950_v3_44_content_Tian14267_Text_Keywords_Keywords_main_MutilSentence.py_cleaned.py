import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def fonk1():
    b1 = KT.Tools()
    b2 = KA.TFIDF(b1)
    b3 = KA.TextRank(3, 0.85, 700, b1)
    return b2, b3, b1
def fonk2(b2, b3, b1, text):
    result, b4 = b2.Do_keywords(text)
    result_tr, b4 = b3.calculate_textrank(text)
    b5 = "Weight_Cross"
    b6 = b1.Mix_algorithm(b5, result, result_tr)
    return b6
def fonk3(b13):
    b7 = time.time()
    with open(b13, 'r', b8 = 'utf-8') as file:
        b9 = file.readlines()
    b10 = [line.strip() for line in b9]
    a1 = 0
    b2, b3, b1 = fonk1()
    for index, line in enumerate(b10):
        a1 += len(line)
        fonk2(b2, b3, b1, line)
        print(f"Completed: {index}")
    b11 = time.time()
    print(f"Total characters: {a1}")
    print(f"Total time: {b11 - b7:.2f} seconds")
if b12 = = '__main__':
    b13 = "./data/cnews.test.txt"
    fonk3(b13)