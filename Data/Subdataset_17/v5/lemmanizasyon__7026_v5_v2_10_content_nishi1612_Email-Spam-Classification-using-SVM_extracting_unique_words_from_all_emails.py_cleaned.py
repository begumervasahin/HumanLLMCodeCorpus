import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join([char for char in text if char not in string.punctuation])
    stop_words = set(stopwords.words('english'))
    text_without_stopwords = ' '.join([word for word in text_without_punctuation.split()
                                       if word.lower() not in stop_words])
    cleaned_words = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_words
def process_files(directory_path):
    lemmatizer = WordNetLemmatizer()
    word_count = {}
    files_processed = 0
    for file in os.listdir(os.fsencode(directory_path)):
        file_name = os.fsdecode(file)
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
            words = text_cleanup(file.read())
            for word in words:
                if not (word.isdigit() or len(word) <= 2):
                    lemmatized_word = lemmatizer.lemmatize(word)
                    word_count[lemmatized_word] = word_count.get(lemmatized_word, 0) + 1
        files_processed += 1
        if files_processed % 100 == 0:
            print(f"Processed {files_processed} files")
    return word_count
def save_word_count_to_csv(word_count, output_file_path, threshold=100):
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    with open(output_file_path, "w+") as output_file:
        output_file.write('word,count\n')
        for word, count in sorted_word_count:
            if count < threshold:
                break
            output_file.write(f"{word},{count}\n")
if __name__ == "__main__":
    start_time = time.time()
    directory_path = "emails/"
    word_count = process_files(directory_path)
    output_file_path = "wordslist.csv"
    save_word_count_to_csv(word_count, output_file_path)
    processing_time = round(time.time() - start_time, 2)
    print(f'Time taken to preprocess emails: {processing_time} seconds')