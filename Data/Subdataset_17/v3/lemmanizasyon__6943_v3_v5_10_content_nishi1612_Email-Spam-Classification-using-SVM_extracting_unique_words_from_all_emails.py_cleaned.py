import os
import time
import string
import operator
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text = ''.join(char for char in text if char not in string.punctuation)
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word.lower() not in stop_words)
    lemmatizer = WordNetLemmatizer()
    cleaned_text = [lemmatizer.lemmatize(word.lower()) for word in text.split()]
    return cleaned_text
def process_files(directory_path):
    start_time = time.time()
    file_count = 0
    word_count = {}
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
            words = text_cleanup(file.read())
            for word in words:
                if not word.isdigit() and len(word) > 2:
                    word_count[word] = word_count.get(word, 0) + 1
            file_count += 1
            if file_count % 100 == 0:
                print(f"Processed {file_count} files")
    sorted_word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))
    with open("wordslist.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for word, count in sorted_word_count.items():
            if count < 100:
                break
            writer.writerow([word, count])
    elapsed_time = round(time.time() - start_time, 2)
    print(f'Time taken to preprocess emails: {elapsed_time} seconds')
if __name__ == "__main__":
    directory_path = "emails/"
    process_files(directory_path)