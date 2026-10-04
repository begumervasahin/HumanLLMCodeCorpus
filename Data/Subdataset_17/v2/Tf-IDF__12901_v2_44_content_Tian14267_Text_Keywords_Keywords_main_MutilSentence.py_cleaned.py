import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def pred_model():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(3, 0.85, 700, tools)
    return tf_idf, tr, tools
def mix_keywords(tf_idf, tr, tools, text):
    result, result_sort = tf_idf.Do_keywords(text)
    result_tr, result_tr_sort = tr.calculate_textrank(text)
    method_num = "Weight_Cross"
    mix_result = tools.Mix_algorithm(method_num, result, result_tr)
    return mix_result
if __name__ == '__main__':
    path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = [line.strip().replace('\n', '') for line in lines]
    all_characters = 0
    tf_idf, tr, tools = pred_model()
    for i, one_line in enumerate(new_lines):
        all_characters += len(one_line)
        mix_keywords(tf_idf, tr, tools, one_line)
        print(f"Completed: {i}")
    end_time = time.time()
    print(f"Total characters: {all_characters}")
    print(f"Total time: {end_time - start_time} seconds")