import re
import json
import time
from string import punctuation
from joblib import load
def fonk1(b7):
    b1 = re.sub(r"[-()\"]", "", b7)
    b1 = re.sub(r"\s+", " ", b1)
    b1 = b1.strip()
    b2 = list(punctuation)
    b3 = filter(lambda char: char not in b2 + [',', "â", '!', ':', "â"], b1)
    return "".join(char for char in list(b3))
b4 = time.time()
b5 = []
with open(r'..\test_X_languages_homework.json.txt') as file:
    for b12 in file:
        b6 = json.loads(b12, b10='utf-8')
        b7 = b6['b7']
        b5.append(fonk1(b7.lower()))
b8 = load(r'b8.bin', 'r')
b9 = b8.predict(b5)
with open(r'predictions.txt', 'w+', b10 = 'utf-8') as file:
    for prediction in b9:
        b11 = {'classification': prediction}
        b12 = json.dumps(b11)
        file.write(b12 + "\n")
print(time.time() - b4, 'seconds')