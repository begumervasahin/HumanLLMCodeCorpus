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
    result, result_sort = tf_idf.Do_keywords(file)
    result_tr, result_tr_sort = tr.calculate_textrank(file)
    method_num = "Weight_Cross"
    mix_result = tools.Mix_algorithm(method_num, result, result_tr)
if __name__ == '__main__':
    path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip().replace('\n', '') for line in lines]
    all_characters = 0
    tf_idf_model, tr_model, tools_model = initialize_models()
    for index, line in enumerate(cleaned_lines):
        all_characters += len(line)
        mix_keywords(tf_idf_model, tr_model, tools_model, line)
        print("Completed:", index)
    end_time = time.time()
    print("Total characters processed:", all_characters)
    print("Total time taken:", (end_time - start_time))