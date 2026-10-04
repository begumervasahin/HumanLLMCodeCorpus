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
    counter = {}
    check_doc = {}
    total_files = 0
    for file in file_list:
        with open(file) as f:
            for line in f:
                jfile = json.loads(line)
                text = jfile.get('desc')
                if text:
                    total_files += 1
                    check_word = {}
                    for word in text.split():
                        if "," not in word and "-" not in word:
                            counter[word] = counter.get(word, 0) + 1
                            check_word[word] = check_word.get(word, 0) + 1
                    for word in check_word:
                        check_doc[word] = check_doc.get(word, 0) + 1
    return counter, check_doc
def compute_result(counter, check_doc):
    result = {}
    for word in check_doc:
        result[word] = counter[word] * check_doc[word] ** 2
    return result
def main():
    directory = 'extracted'
    file_list = list_files(directory)
    file_list = ['out.txt']
    counter, check_doc = process_files(file_list)
    result = compute_result(counter, check_doc)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    for i, (word, score) in enumerate(sorted_result[:50]):
        print(word)
if __name__ == "__main__":
    main()