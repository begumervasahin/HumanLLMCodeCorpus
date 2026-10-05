import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def fonk1():
    b1 = KT.Tools()
    b2 = KA.TFIDF(b1)
    b3 = KA.TextRank(window_size=3, damping_factor=0.85, max_iterations=700, b1=b1)
    return b2, b3, b1
def fonk2(b2, b3, b1, text):
    result_tf_idf, b4 = b2.Do_keywords(text)
    result_tr, b4 = b3.calculate_textrank(text)
    b5 = "Weight_Cross"
    b6 = b1.Mix_algorithm(b5, result_tf_idf, result_tr)
if b7 = = '__main__':
    b8 = "./data/cnews.test.txt"
    b9 = time.time()
    with open(b8, 'r', b10 = 'utf-8') as file:
        b11 = file.readlines()
        b12 = [line.strip() for line in b11]
    tf_idf_model, tr_model, b13 = fonk1()
    a1 = 0
    for index, line in enumerate(b12):
        a1 += len(line)
        fonk2(tf_idf_model, tr_model, b13, line)
        print("Completed:", index)
    b14 = time.time()
    print("Total characters processed:", a1)
    print("Total time taken:", (b14 - b9))