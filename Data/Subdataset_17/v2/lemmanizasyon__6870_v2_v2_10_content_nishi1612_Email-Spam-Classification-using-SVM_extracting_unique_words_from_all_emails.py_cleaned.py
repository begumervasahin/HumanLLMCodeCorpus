import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join(char for char in text if char not in string.punctuation)
    text_without_stopwords = ' '.join(
        word for word in text_without_punctuation.split() if word.lower() not in stopwords.words('english')
    )
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
def process_emails(directory_path, output_file_path, lemmatizer):
    start_time = time.time()
    word_count = {}
    processed_files_count = 0
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
            words = text_cleanup(file_reading.read())
            for word in words:
                if not (word.isdigit() or len(word) <= 2):
                    lemmatized_word = lemmatizer.lemmatize(word)
                    word_count[lemmatized_word] = word_count.get(lemmatized_word, 0) + 1
        processed_files_count += 1
        if processed_files_count % 100 == 0:
            print(f"Processed {processed_files_count} files")
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    with open(output_file_path, "w+", encoding='utf-8') as output_file:
        output_file.write('word,count\n')
        for word, count in sorted_word_count:
            if count < 100:
                break
            output_file.write(f"{word},{count}\n")
    processing_time = round(time.time() - start_time, 2)
    print(f'Time taken to preprocess emails: {processing_time} seconds')
if __name__ == "__main__":
    directory_path = "emails/"
    output_file_path = "wordslist.csv"
    lemmatizer = WordNetLemmatizer()
    process_emails(directory_path, output_file_path, lemmatizer)