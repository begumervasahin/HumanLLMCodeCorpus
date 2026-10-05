import re
import json
import time
from string import punctuation
from joblib import load
def fonk1(text):
    b1 = re.sub(r"[-()\"]", "", text)
    b1 = re.sub(r"\s+", " ", b1)
    return b1.strip()
def fonk2(text):
    b2 = list(punctuation)
    return filter(lambda x: x not in b2 + [',', "â", '!', ':', "â"], text)
b3 = time.process_time()
b4 = []
with open('test_X_languages_homework.json.txt', b5 = 'utf-8') as file:
    for line in file:
        b6 = json.loads(line)
        b7 = fonk1(b6['text'])
        b7 = "".join(fonk2(b7)).lower()
        b4.append(b7)
b8 = load('model.bin')
b9 = b8.predict(b4)
with open('predictions.txt', 'w+', b5 = 'utf-8') as output_file:
    for label in b9:
        json.dump({'classification': label}, output_file)
        output_file.write('\n')
print("Execution time:", time.process_time() - b3, 'seconds')