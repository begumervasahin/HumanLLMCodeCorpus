import os
import json
import operator
def list_files(dir):
    file_list = []
    for subdir, _, files in os.walk(dir):
        for file in files:
            file_list.append(os.path.join(subdir, file))
    return file_list
file_paths = list_files('extracted')
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
result = {}
for word in document_count:
    result[word] = word_count[word] * document_count[word] ** 2
sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
for i, (word, score) in enumerate(sorted_result[:50]):
    print(f"{word}: {score}")
for word, _ in sorted_result[:50]:
    print(word)