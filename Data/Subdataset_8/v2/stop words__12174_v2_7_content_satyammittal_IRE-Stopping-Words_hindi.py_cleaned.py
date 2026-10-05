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
    word_counts = {}
    doc_frequencies = {}
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                json_data = json.loads(line)
                text = json_data.get('text', '')
                for word in text.split():
                    word_counts[word] = word_counts.get(word, 0) + 1
                    doc_frequencies[word] = doc_frequencies.get(word, 0) + 1
    scores = {}
    for word in doc_frequencies:
        scores[word] = word_counts[word] * doc_frequencies[word] * doc_frequencies[word]
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    for word, score in sorted_scores[:50]:
        print(f"{word}: {score}")
if __name__ == "__main__":
    main()