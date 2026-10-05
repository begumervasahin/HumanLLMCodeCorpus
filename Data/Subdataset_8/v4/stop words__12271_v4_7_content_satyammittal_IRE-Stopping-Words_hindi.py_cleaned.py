import os
import json
import operator
def list_files(directory):
    file_list = []
    subdirectories = [x[0] for x in os.walk(directory)]
    for subdir in subdirectories:
        files = os.walk(subdir).__next__()[2]
        if len(files) > 0:
            for file in files:
                file_list.append(os.path.join(subdir, file))
    return file_list
file_paths = list_files('extracted')
word_frequency = {}
document_frequency = {}
for file_path in file_paths:
    with open(file_path) as file:
        for line in file:
            word_count_in_current_doc = {}
            json_data = json.loads(line)
            text = json_data.get('text', None)
            if text is not None:
                for word in text.split():
                    word_frequency[word] = word_frequency.get(word, 0) + 1
                    word_count_in_current_doc[word] = word_count_in_current_doc.get(word, 0) + 1
                for word in word_count_in_current_doc:
                    document_frequency[word] = document_frequency.get(word, 0) + 1
result = {}
for word, doc_freq in document_frequency.items():
    result[word] = word_frequency[word] * doc_freq * doc_freq
sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
top_words_count = 50
for word, score in sorted_result[:top_words_count]:
    print(word, ':', score)
print('\nTop 50 words:')
for word, _ in sorted_result[:top_words_count]:
    print(word)