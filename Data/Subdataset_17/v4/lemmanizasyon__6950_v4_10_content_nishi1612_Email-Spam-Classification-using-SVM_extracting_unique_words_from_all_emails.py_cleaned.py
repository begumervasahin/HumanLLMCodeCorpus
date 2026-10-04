import os
import nltk
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
def main():
    start_time = time.time()
    lmtzr = WordNetLemmatizer()
    count = {}
    directory_in_str = "emails/"
    directory = os.fsencode(directory_in_str)
    k = 0
    for file in os.listdir(directory):
        file_name = os.path.join(directory_in_str, file.decode("utf-8"))
        with open(file_name, "r", encoding='utf-8', errors='ignore') as file_reading:
            words = text_cleanup(file_reading.read())
            for word in words:
                if not word.isdigit() and len(word) > 2:
                    word = lmtzr.lemmatize(word)
                    count[word] = count.get(word, 0) + 1
        k += 1
        if k % 100 == 0:
            print(f"Processed {k} files")
    sorted_count = dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True))
    with open("wordslist.csv", "w+") as f:
        f.write('word,count\n')
        for word, times in sorted_count.items():
            if times < 100:
                break
            f.write(f"{word},{times}\n")
    print(f'Time (in seconds) to preprocess the emails: {round(time.time() - start_time, 2)}')
if __name__ == "__main__":
    main()