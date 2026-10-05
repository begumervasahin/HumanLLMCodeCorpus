import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def initialize_models():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(3, 0.85, 700, tools)
    return tf_idf, tr, tools
def mix_keywords(tf_idf, tr, tools, file):
    result_tf_idf, _ = tf_idf.Do_keywords(file)
    result_tr, _ = tr.calculate_textrank(file)
    method_num = "Weight_Cross"
    mix_result = tools.Mix_algorithm(method_num, result_tf_idf, result_tr)
if __name__ == '__main__':
    path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        new_lines = [line.strip().replace('\n', '') for line in lines]
    file.close()
    tf_idf, tr, tools = initialize_models()
    total_characters = 0
    for i, line in enumerate(new_lines):
        total_characters += len(line)
        mix_keywords(tf_idf, tr, tools, line)
        print("Completed:", i)
    end_time = time.time()
    print("Total characters:", total_characters)
    print("Total time taken:", (end_time - start_time))