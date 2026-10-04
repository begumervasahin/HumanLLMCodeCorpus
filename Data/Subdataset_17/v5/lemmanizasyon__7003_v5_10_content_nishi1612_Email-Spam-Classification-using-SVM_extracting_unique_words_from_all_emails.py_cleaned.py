import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join([c for c in text if c not in string.punctuation])
    stop_words = set(stopwords.words('english'))
    text_without_stopwords = ' '.join([word for word in text_without_punctuation.split() if word.lower() not in stop_words])
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
def process_files(directory):
    lmtzr = WordNetLemmatizer()
    word_count = {}
    for idx, file in enumerate(os.listdir(directory)):
        file_path = os.path.join(directory, file.decode("utf-8"))
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
            words = text_cleanup(file_reading.read())
            for word in words:
                if not word.isdigit() and len(word) > 2:
                    lemmatized_word = lmtzr.lemmatize(word)
                    word_count[lemmatized_word] = word_count.get(lemmatized_word, 0) + 1
        if (idx + 1) % 100 == 0:
            print(f"Processed {idx + 1} files")
    return word_count
def save_word_count(word_count, output_file, min_count=100):
    sorted_word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))
    with open(output_file, "w+") as f:
        f.write('word,count\n')
        for word, count in sorted_word_count.items():
            if count < min_count:
                break
            f.write(f"{word},{count}\n")
def main():
    start_time = time.time()
    input_directory = "emails/"
    output_file = "wordslist.csv"
    word_count = process_files(os.fsencode(input_directory))
    save_word_count(word_count, output_file)
    elapsed_time = round(time.time() - start_time, 2)
    print(f'Time (in seconds) to preprocess the emails: {elapsed_time}')
if __name__ == "__main__":
    main()