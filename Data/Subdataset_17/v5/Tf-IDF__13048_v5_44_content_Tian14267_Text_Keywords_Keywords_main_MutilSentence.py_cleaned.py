import time
import Keywords_Algorithm as KA
import keywords_tools as KT
def initialize_models():
    tools = KT.Tools()
    tf_idf = KA.TFIDF(tools)
    text_rank = KA.TextRank(3, 0.85, 700, tools)
    return tf_idf, text_rank, tools
def process_text(tf_idf, text_rank, tools, text):
    tf_idf_results, _ = tf_idf.Do_keywords(text)
    text_rank_results, _ = text_rank.calculate_textrank(text)
    method = "Weight_Cross"
    return tools.Mix_algorithm(method, tf_idf_results, text_rank_results)
def main():
    file_path = "./data/cnews.test.txt"
    start_time = time.time()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_lines = [line.strip() for line in lines]
    total_characters = 0
    tf_idf, text_rank, tools = initialize_models()
    for index, line in enumerate(cleaned_lines):
        total_characters += len(line)
        process_text(tf_idf, text_rank, tools, line)
        print(f"Progress: Line {index + 1}/{len(cleaned_lines)}")
    end_time = time.time()
    print(f"Total Characters: {total_characters}")
    print(f"Total Time Elapsed: {end_time - start_time:.2f} seconds")
if __name__ == '__main__':
    main()