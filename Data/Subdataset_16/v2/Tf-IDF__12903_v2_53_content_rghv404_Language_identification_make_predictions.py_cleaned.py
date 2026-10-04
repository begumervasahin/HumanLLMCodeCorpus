import re
import json
import time
from string import punctuation
from joblib import load
def fonk1(b1):
    b1 = re.sub(r"[-()\"
    b1 = re.sub(r"\s+", " ", b1)
    b1 = b1.strip()
    b2 = set(punctuation) | {',', "â", '!', ':', "â"}
    b3 = ''.join(char for char in b1 if char not in b2)
    return b3.lower()
def fonk2():
    b4 = time.time()
    b5 = []
    with open(r'..\test_X_languages_homework.json.txt', 'r', b6 = 'utf-8') as file:
        for line in file:
            b7 = json.loads(line)
            b8 = b7.get('b1', '')
            b9 = fonk1(b8)
            b5.append(b9)
    b10 = load(r'model.bin')
    b11 = b10.predict(b5)
    with open(r'b12.txt', 'w', b6 = 'utf-8') as file:
        for prediction in b11:
            b12 = {'classification': prediction}
            b13 = json.dumps(b12)
            file.write(b13 + "\n")
    b14 = time.time() - b4
    print(f"{b14:.2f} seconds")
if b15 = = "__main__":
    fonk2()