import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def initialize_models():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(window_size=3, damping_factor=0.85, max_iterations=700, tools=tools)
    return tf_idf, tr, tools
def extract_keywords(tf_idf, tr, tools, text):
    result_tf_idf, _ = tf_idf.Do_keywords(text)
    result_tr, _ = tr.calculate_textrank(text)
    method = "Weight_Cross"
    mixed_result = tools.Mix_algorithm(method, result_tf_idf, result_tr)
if __name__ == '__main__':
    file_path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines]
    tf_idf_model, tr_model, tools_model = initialize_models()
    total_characters = 0
    for index, line in enumerate(cleaned_lines):
        total_characters += len(line)
        extract_keywords(tf_idf_model, tr_model, tools_model, line)
        print("Completed:", index)
    end_time = time.time()
    print("Total characters processed:", total_characters)
    print("Total time taken:", (end_time - start_time))