import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def initialize_models():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    tr = KA.TextRank(window_size=3, damping_factor=0.85, max_iterations=700, tools=tools)
    return tf_idf, tr, tools
def mix_keywords(tf_idf, tr, tools, text):
    result_tf_idf, _ = tf_idf.Do_keywords(text)
    result_tr, _ = tr.calculate_textrank(text)
    mix_result = tools.Mix_algorithm(method_num="Weight_Cross", result1=result_tf_idf, result2=result_tr)
if __name__ == '__main__':
    path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    tf_idf, tr, tools = initialize_models()
    total_characters = sum(len(line) for line in lines)
    for i, line in enumerate(lines):
        mix_keywords(tf_idf, tr, tools, line)
        print("Completed:", i)
    end_time = time.time()
    print("Total characters:", total_characters)
    print("Total time taken:", (end_time - start_time))