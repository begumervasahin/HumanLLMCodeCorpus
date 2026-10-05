import os
import json
import operator
def list_files(directory):
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list
def main():
    directory = 'extracted'
    files = list_files(directory)
    counter = {}
    check_doc = {}
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                check_word = {}
                jfile = json.loads(line)
                text = jfile.get('text', '')
                for word in text.split():
                    counter[word] = counter.get(word, 0) + 1
                    check_word[word] = check_word.get(word, 0) + 1
                for word in check_word:
                    check_doc[word] = check_doc.get(word, 0) + 1
    result = {}
    for word in check_doc:
        result[word] = counter[word] * check_doc[word] * check_doc[word]
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    for word, count in sorted_result[:50]:
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()