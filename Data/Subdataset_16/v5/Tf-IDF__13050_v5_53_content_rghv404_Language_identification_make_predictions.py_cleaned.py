import re
import json
import time
from string import punctuation
from joblib import load
def fonk1(file_path):
    with open(file_path, 'r', b1 = 'utf-8') as file:
        b2 = file.readlines()
        b3 = [fonk2(json.loads(line)['b4']) for line in b2]
    return b3
def fonk2(b4):
    b4 = re.sub(r"[-()\"
    b4 = re.sub(r"\s+", " ", b4).strip()
    b5 = set(punctuation + ',â!:â')
    b6 = ''.join(char for char in b4 if char not in b5)
    return b6.lower()
def fonk3(predictions, file_path):
    with open(file_path, 'w', b1 = 'utf-8') as file:
        for prediction in predictions:
            b7 = json.dumps({'classification': prediction})
            file.write(b7 + "\n")
def fonk4():
    b8 = time.time()
    b9 = r'..\test_X_languages_homework.json.txt'
    b10 = fonk1(b9)
    b11 = r'b12.bin'
    b12 = load(b11)
    b13 = b12.predict(b10)
    b14 = r'predictions.txt'
    fonk3(b13, b14)
    print(f"{time.time() - b8} seconds")
if b15 = = "__main__":
    fonk4()