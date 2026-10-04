import os
import json
import operator
def list_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
def process_files(file_paths):
    word_counter = {}
    doc_frequency = {}
    total_docs = 0
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                check_word = {}
                json_data = json.loads(line)
                text = json_data.get('text')
                total_docs += 1
                if text:
                    for word in text.split():
                        word_counter[word] = word_counter.get(word, 0) + 1
                        check_word[word] = check_word.get(word, 0) + 1
                for word in check_word:
                    doc_frequency[word] = doc_frequency.get(word, 0) + 1
    return word_counter, doc_frequency
def calculate_scores(word_counter, doc_frequency):
    scores = {}
    for word in doc_frequency:
        scores[word] = word_counter[word] * (doc_frequency[word] ** 2)
    return scores
def main():
    directory = 'extracted'
    files = list_files(directory)
    word_counter, doc_frequency = process_files(files)
    scores = calculate_scores(word_counter, doc_frequency)
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print("Top 50 words and their scores:")
    for word, score in sorted_scores[:50]:
        print(f"{word} : {score}")
    print("\nTop 50 words:")
    for word, _ in sorted_scores[:50]:
        print(word)
if __name__ == "__main__":
    main()