import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join([char for char in text if char not in string.punctuation])
    words_without_stopwords = [word for word in text_without_punctuation.split() if word.lower() not in stopwords.words('english')]
    cleaned_text = [word.lower() for word in words_without_stopwords]
    return cleaned_text
def lemmatize_and_count(words, lemmatizer, word_count):
    for word in words:
        if not (word.isdigit() or len(word) <= 2):
            lemmatized_word = lemmatizer.lemmatize(word)
            word_count[lemmatized_word] = word_count.get(lemmatized_word, 0) + 1
def process_directory(directory_path):
    word_count = {}
    lemmatizer = WordNetLemmatizer()
    k = 0
    for file in os.listdir(directory_path):
        file_path = os.path.join(os.getcwd(), 'emails', file.decode("utf-8"))
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
            words = text_cleanup(file_reading.read())
            lemmatize_and_count(words, lemmatizer, word_count)
        k += 1
        if k % 100 == 0:
            print(f"Processed {k} files")
    return word_count
def write_to_csv(sorted_word_count, output_file_path):
    with open(output_file_path, "w+") as output_file:
        output_file.write('word,count\n')
        for word, count in sorted_word_count.items():
            if count < 100:
                break
            output_file.write(f"{word},{count}\n")
def main():
    start_time = time.time()
    directory_path = "emails/"
    word_count = process_directory(directory_path)
    sorted_word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))
    write_to_csv(sorted_word_count, "wordslist.csv")
    processing_time = round(time.time() - start_time, 2)
    print(f'Time taken to preprocess emails: {processing_time} seconds')
if __name__ == "__main__":
    main()