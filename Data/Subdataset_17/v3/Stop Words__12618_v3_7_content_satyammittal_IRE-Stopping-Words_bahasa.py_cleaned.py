import os
import json
import operator
def list_files(dir_path):
    file_list = []
    for subdir, _, files in os.walk(dir_path):
        for file in files:
            file_list.append(os.path.join(subdir, file))
    return file_list
def process_files(file_list):
    word_counter = {}
    document_counter = {}
    for file in file_list:
        try:
            with open(file, 'r') as f:
                for line in f:
                    jfile = json.loads(line)
                    text = jfile.get('desc')
                    if text:
                        unique_words = set()
                        for word in text.split():
                            cleaned_word = word.strip(",.-")
                            if cleaned_word:
                                word_counter[cleaned_word] = word_counter.get(cleaned_word, 0) + 1
                                unique_words.add(cleaned_word)
                        for word in unique_words:
                            document_counter[word] = document_counter.get(word, 0) + 1
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error processing file {file}: {e}")
    return word_counter, document_counter
def calculate_scores(word_counter, document_counter):
    scores = {
        word: count * (doc_count ** 2)
        for word, count in word_counter.items()
        for doc_count in [document_counter[word]]
    }
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_scores
def main():
    dir_path = 'extracted'
    file_list = list_files(dir_path)
    file_list = ['out.txt']
    word_counter, document_counter = process_files(file_list)
    sorted_scores = calculate_scores(word_counter, document_counter)
    top_n = 50
    for i, (word, score) in enumerate(sorted_scores):
        if i >= top_n:
            break
        print(word)
if __name__ == "__main__":
    main()