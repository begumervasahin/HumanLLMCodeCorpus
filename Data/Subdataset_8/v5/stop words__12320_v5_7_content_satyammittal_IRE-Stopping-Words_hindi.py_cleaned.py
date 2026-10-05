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
    word_frequency = {}
    document_frequency = {}
    for file_path in file_paths:
        with open(file_path) as file:
            for line in file:
                json_data = json.loads(line)
                text = json_data.get('text', None)
                if text is not None:
                    word_count_in_current_doc = {}
                    for word in text.split():
                        word_frequency[word] = word_frequency.get(word, 0) + 1
                        word_count_in_current_doc[word] = word_count_in_current_doc.get(word, 0) + 1
                    for word in word_count_in_current_doc:
                        document_frequency[word] = document_frequency.get(word, 0) + 1
    return word_frequency, document_frequency
def calculate_scores(word_frequency, document_frequency):
    result = {}
    for word, doc_freq in document_frequency.items():
        result[word] = word_frequency[word] * doc_freq * doc_freq
    return result
def print_top_words(sorted_result, top_words_count):
    print("Top 50 words with their scores:")
    for word, score in sorted_result[:top_words_count]:
        print(f"{word}: {score}")
    print("\nTop 50 words without their scores:")
    for word, _ in sorted_result[:top_words_count]:
        print(word)
def main():
    file_paths = list_files('extracted')
    word_frequency, document_frequency = process_files(file_paths)
    result = calculate_scores(word_frequency, document_frequency)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    top_words_count = 50
    print_top_words(sorted_result, top_words_count)
if __name__ == "__main__":
    main()