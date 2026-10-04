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
def fonk2(file_path):
    b4 = []
    with open(file_path, 'r', b5 = 'utf-8') as file:
        for line in file:
            b6 = json.loads(line)
            b7 = b6.get('b1', '')
            b3 = fonk1(b7)
            b4.append(b3)
    return b4
def fonk3(predictions, output_path):
    with open(output_path, 'w', b5 = 'utf-8') as file:
        for prediction in predictions:
            b8 = {'classification': prediction}
            b9 = json.dumps(b8)
            file.write(b9 + "\n")
def fonk4():
    b10 = time.time()
    b11 = r'..\test_X_languages_homework.json.txt'
    b12 = r'predictions.txt'
    b13 = r'b14.bin'
    b4 = fonk2(b11)
    b14 = load(b13)
    b15 = b14.predict(b4)
    fonk3(b15, b12)
    b16 = time.time() - b10
    print(f"Execution Time: {b16:.2f} seconds")
if b17 = = "__main__":
    fonk4()