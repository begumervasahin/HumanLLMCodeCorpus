import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def Pred_model():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(3, 0.85, 700, tools)
    return tf_idf, tr, tools
def Mix_keywords(tf_idf, tr, tools, file):
    result, result_sort = tf_idf.Do_keywords(file)
    result_tr, result_tr_sort = tr.calculate_textrank(file)
    method_num = "Weight_Cross"
    mix_result = tools.Mix_algorithm(method_num, result, result_tr)
if __name__ == '__main__':
    path = "./data/cnews.test.txt"
    start = time.time()
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = [line.strip().replace('\n', '') for line in lines]
    all_character = 0
    tf_idf, tr, tools = Pred_model()
    for i, one_line in enumerate(new_lines):
        all_character += len(one_line)
        Mix_keywords(tf_idf, tr, tools, one_line)
        print("å®æï¼", i)
    end = time.time()
    print("æ»å­æ°ï¼", all_character)
    print("æ»æ¶é´ï¼", (end - start))