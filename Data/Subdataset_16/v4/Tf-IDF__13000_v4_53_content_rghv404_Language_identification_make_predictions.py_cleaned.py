import re
import json
import time
from string import punctuation
from joblib import load
b1 = time.time()
b2 = []
with open(r'..\test_X_languages_homework.json.txt', 'r', b3 = 'utf-8') as f:
    b4 = f.readlines()
    for j_obj in b4:
        b5 = json.loads(j_obj)['text']
        b6 = re.sub(r"[-()\"
        b6 = re.sub(r"\s+", " ", b6)
        b6 = b6.strip()
        b7 = set(punctuation + ',â!:â')
        b8 = ''.join(ch for ch in b6 if ch not in b7)
        b2.append(b8.lower())
b9 = load(r'model.bin')
b10 = b9.predict(b2)
with open(r'b11.txt', 'w', b3 = 'utf-8') as f:
    for y in b10:
        b11 = {'classification': y}
        b12 = json.dumps(b11)
        f.write(b12 + "\n")
print(f"{time.time() - b1} seconds")