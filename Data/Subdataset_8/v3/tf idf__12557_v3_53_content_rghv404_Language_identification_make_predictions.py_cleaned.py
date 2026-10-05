import re
import json
import time
from string import punctuation
from joblib import load
def clean_text(text):
    cleaned_text = re.sub(r"[-()\"]", "", text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    return cleaned_text.strip()
def filter_punctuation(text):
    punc = list(punctuation)
    return filter(lambda x: x not in punc + [',', "â", '!', ':', "â"], text)
start_time = time.process_time()
x_test = []
with open('test_X_languages_homework.json.txt', encoding='utf-8') as file:
    for line in file:
        feature = json.loads(line)
        cleaned_feature = clean_text(feature['text'])
        cleaned_feature = "".join(filter_punctuation(cleaned_feature)).lower()
        x_test.append(cleaned_feature)
pipe = load('model.bin')
y_predicted = pipe.predict(x_test)
with open('predictions.txt', 'w+', encoding='utf-8') as output_file:
    for label in y_predicted:
        json.dump({'classification': label}, output_file)
        output_file.write('\n')
print("Execution time:", time.process_time() - start_time, 'seconds')