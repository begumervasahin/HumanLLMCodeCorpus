import numpy as np
import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def initialize_models():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(3, 0.85, 700, tools)
    return tf_idf, tr, tools
def extract_and_combine_keywords(tf_idf, tr, tools, text):
    result, _ = tf_idf.Do_keywords(text)
    result_tr, _ = tr.calculate_textrank(text)
    method_num = "Weight_Cross"
    combined_result = tools.Mix_algorithm(method_num, result, result_tr)
    return combined_result
def process_file_lines(file_path):
    start_time = time.time()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_lines = [line.strip() for line in lines]
    total_characters = 0
    tf_idf, tr, tools = initialize_models()
    for index, line in enumerate(cleaned_lines):
        total_characters += len(line)
        extract_and_combine_keywords(tf_idf, tr, tools, line)
        print(f"Completed: {index}")
    end_time = time.time()
    print(f"Total characters: {total_characters}")
    print(f"Total time: {end_time - start_time:.2f} seconds")
if __name__ == '__main__':
    file_path = "./data/cnews.test.txt"
    process_file_lines(file_path)