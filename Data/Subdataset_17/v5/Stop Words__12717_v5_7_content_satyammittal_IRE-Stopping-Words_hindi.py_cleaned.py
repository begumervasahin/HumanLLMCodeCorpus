import os
import json
import operator
def list_files(directory):
    file_list = []
    for subdir, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(subdir, file))
    return file_list
def process_files(file_paths):
    word_count = {}
    document_count = {}
    total_documents = 0
    for file in file_paths:
        with open(file) as f:
            for line in f:
                word_in_document = {}
                json_line = json.loads(line)
                text = json_line.get('text')
                if text:
                    total_documents += 1
                    for word in text.split():
                        word_count[word] = word_count.get(word, 0) + 1
                        word_in_document[word] = word_in_document.get(word, 0) + 1
                for word in word_in_document:
                    document_count[word] = document_count.get(word, 0) + 1
    return word_count, document_count
def calculate_result(word_count, document_count):
    result = {}
    for word in document_count:
        result[word] = word_count[word] * (document_count[word] ** 2)
    return result
def main():
    file_paths = list_files('extracted')
    word_count, document_count = process_files(file_paths)
    result = calculate_result(word_count, document_count)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    print("Top 50 words with their scores:")
    for word, score in sorted_result[:50]:
        print(f"{word}: {score}")
    print("\nTop 50 words:")
    for word, _ in sorted_result[:50]:
        print(word)
if __name__ == "__main__":
    main()