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
    b5 = b1.Mix_algorithm(method_num="Weight_Cross", result1=result_tf_idf, result2=result_tr)
if b6 = = '__main__':
    b7 = "./data/cnews.test.txt"
    b8 = time.time()
    with open(b7, 'r', b9 = 'utf-8') as file:
        b10 = [line.strip() for line in file.readlines()]
    b2, b3, b1 = fonk1()
    b11 = sum(len(line) for line in b10)
    for i, line in enumerate(b10):
        fonk2(b2, b3, b1, line)
        print("Completed:", i)
    b12 = time.time()
    print("Total characters:", b11)
    print("Total time taken:", (b12 - b8))