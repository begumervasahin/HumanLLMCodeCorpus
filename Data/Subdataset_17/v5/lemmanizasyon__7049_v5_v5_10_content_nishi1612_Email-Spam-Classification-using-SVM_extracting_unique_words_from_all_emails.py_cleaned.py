import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join(char for char in text if char not in string.punctuation)
    stop_words = set(stopwords.words('english'))
    text_without_stopwords = ' '.join(word for word in text_without_punctuation.split() if word.lower() not in stop_words)
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
def process_files(directory_path, lemmatizer):
    word_count = {}
    file_count = 0
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file.decode("utf-8"))
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reader:
            words = text_cleanup(file_reader.read())
            for word in words:
                if not word.isdigit() and len(word) > 2:
                    lemmatized_word = lemmatizer.lemmatize(word)
                    word_count[lemmatized_word] = word_count.get(lemmatized_word, 0) + 1
            file_count += 1
            if file_count % 100 == 0:
                print(f"Processed {file_count} files")
    return word_count, file_count
def write_word_count_to_csv(word_count, filename="wordslist.csv", min_count=100):
    sorted_word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))
    with open(filename, "w", newline='', encoding='utf-8') as csv_file:
        csv_file.write('word,count\n')
        for word, count in sorted_word_count.items():
            if count < min_count:
                break
            csv_file.write(f"{word},{count}\n")
def main():
    start_time = time.time()
    lemmatizer = WordNetLemmatizer()
    directory_path = "emails/"
    word_count, file_count = process_files(os.fsencode(directory_path), lemmatizer)
    write_word_count_to_csv(word_count)
    elapsed_time = round(time.time() - start_time, 2)
    print(f'Time taken to preprocess {file_count} emails: {elapsed_time} seconds')
if __name__ == "__main__":
    main()