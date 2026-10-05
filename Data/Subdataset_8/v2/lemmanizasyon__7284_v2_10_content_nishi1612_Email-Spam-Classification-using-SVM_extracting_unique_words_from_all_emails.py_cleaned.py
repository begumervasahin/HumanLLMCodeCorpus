import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = ''.join([c for c in text if c not in string.punctuation])
    text_without_stopwords = ' '.join([word for word in text_without_punctuation.split() if word.lower() not in stopwords.words('english')])
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
start_time = time.time()
lemmatizer = WordNetLemmatizer()
k = 0
word_count = {}
directory_path = "emails/"
directory = os.fsencode(directory_path)
for file in os.listdir(directory):
    file = file.decode("utf-8")
    file_path = os.path.join(os.getcwd(), 'emails', file)
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
        words = text_cleanup(file_reading.read())
        for word in words:
            if not (word.isdigit() or len(word) <= 2):
                word = lemmatizer.lemmatize(word)
                word_count[word] = word_count.get(word, 0) + 1
    k += 1
    if k % 100 == 0:
        print(f"Processed {k} files")
sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
sorted_word_count = dict(sorted_word_count)
with open("wordslist.csv", "w+") as output_file:
    output_file.write('word,count\n')
    for word, count in sorted_word_count.items():
        if count < 100:
            break
        output_file.write(f"{word},{count}\n")
processing_time = round(time.time() - start_time, 2)
print(f'Time taken to preprocess emails: {processing_time} seconds')