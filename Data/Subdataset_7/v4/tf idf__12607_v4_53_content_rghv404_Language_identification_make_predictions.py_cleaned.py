import re
import json
import time
from string import punctuation
from joblib import load
b1 = time.time()
b2 = []
with open(r'..\test_X_languages_homework.json.txt') as file:
    for b12 in file.readlines():
        b3 = json.loads(b12, b10='utf-8')
        b4 = b3['b4']
        b5 = re.sub(r"[-()\"]", "", b4)
        b5 = re.sub(r"\s+", " ", b5)
        b5 = b5.strip()
        b6 = list(punctuation)
        b7 = filter(lambda char: char not in b6 + [',', "â", '!', ':', "â"], b5)
        b5 = "".join(char for char in list(b7))
        b2.append(b5.lower())
b8 = load(r'b8.bin', 'r')
b9 = b8.predict(b2)
with open(r'predictions.txt', 'w+', b10 = 'utf-8') as file:
    for prediction in b9:
        b11 = {'classification': prediction}
        b12 = json.dumps(b11)
        file.write(b12 + "\n")
print(time.time() - b1, 'seconds')