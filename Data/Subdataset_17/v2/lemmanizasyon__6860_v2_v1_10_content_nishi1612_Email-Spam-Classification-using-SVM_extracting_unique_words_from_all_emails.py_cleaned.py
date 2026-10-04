import os
import nltk
import time
import string
import operator
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
def text_cleanup(text):
    text_without_punctuation = ''.join([c for c in text if c not in string.punctuation])
    text_without_stopwords = ' '.join([word for word in text_without_punctuation.split()
                                       if word.lower() not in stopwords.words('english')])
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
def main():
    start_time = time.time()
    lemmatizer = WordNetLemmatizer()
    word_count = {}
    processed_files_count = 0
    input_directory = "emails/"
    for file in os.listdir(input_directory):
        file_path = os.path.join(os.getcwd(), input_directory, file)
        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            words = text_cleanup(f.read())
            for word in words:
                if not word.isdigit() and len(word) > 2:
                    lemma = lemmatizer.lemmatize(word)
                    word_count[lemma] = word_count.get(lemma, 0) + 1
        processed_files_count += 1
        if processed_files_count % 100 == 0:
            print(f"Processed {processed_files_count} files")
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    with open("wordslist.csv", "w+", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'count'])
        for word, count in sorted_word_count:
            if count < 100:
                break
            writer.writerow([word, count])
    elapsed_time = round(time.time() - start_time, 2)
    print(f'Time (in seconds) to preprocess the emails: {elapsed_time}')
if __name__ == "__main__":
    main()