import os
import json
import operator
def list_files(directory):
    files_list = []
    for subdir, _, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(subdir, file))
    return files_list
def process_files(file_list):
    word_counter = {}
    document_counter = {}
    total_files = 0
    for file in file_list:
        with open(file) as f:
            for line in f:
                json_data = json.loads(line)
                text = json_data.get('desc')
                if text:
                    total_files += 1
                    local_word_counter = {}
                    for word in text.split():
                        if "," not in word and "-" not in word:
                            word_counter[word] = word_counter.get(word, 0) + 1
                            local_word_counter[word] = local_word_counter.get(word, 0) + 1
                    for word in local_word_counter:
                        document_counter[word] = document_counter.get(word, 0) + 1
    return word_counter, document_counter
def compute_results(word_counter, document_counter):
    results = {}
    for word in document_counter:
        results[word] = word_counter[word] * document_counter[word] ** 2
    return results
def main():
    directory = 'extracted'
    file_list = list_files(directory)
    file_list = ['out.txt']
    word_counter, document_counter = process_files(file_list)
    results = compute_results(word_counter, document_counter)
    sorted_results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
    for i, (word, score) in enumerate(sorted_results[:50]):
        print(word)
if __name__ == "__main__":
    main()