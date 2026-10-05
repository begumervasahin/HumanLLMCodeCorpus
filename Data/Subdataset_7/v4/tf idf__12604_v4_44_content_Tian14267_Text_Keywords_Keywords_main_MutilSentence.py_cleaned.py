import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def fonk1():
    b1 = KT.Tools()
    b2 = KA.TFIDF(b1)
    b3 = KA.TextRank(3, 0.85, 700, b1)
    return b2, b3, b1
def fonk2(b2, b3, b1, file):
    result, b4 = b2.Do_keywords(file)
    result_tr, b5 = b3.calculate_textrank(file)
    b6 = "Weight_Cross"
    b7 = b1.Mix_algorithm(b6, result, result_tr)
if b8 = = '__main__':
    b9 = "./data/cnews.test.txt"
    b10 = time.time()
    with open(b9, 'r', b11 = 'utf-8') as file:
        b12 = file.readlines()
        b13 = [line.strip().replace('\n', '') for line in b12]
    a1 = 0
    tf_idf_model, tr_model, b14 = fonk1()
    for index, line in enumerate(b13):
        a1 += len(line)
        fonk2(tf_idf_model, tr_model, b14, line)
        print("Completed:", index)
    b15 = time.time()
    print("Total characters processed:", a1)
    print("Total time taken:", (b15 - b10))