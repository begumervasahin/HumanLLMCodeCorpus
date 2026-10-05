import re
import json
import time
from string import punctuation
from joblib import load
b1 = time.process_time()
b2 = []
with open('test_X_languages_homework.json.txt', b3 = 'utf-8') as f:
    b4 = f.readlines()
    for j_obj in b4:
        b5 = json.loads(j_obj)
        b5 = b5['text']
        b6 = re.sub(r"[-()\"]", "", b5)
        b6 = re.sub(r"\s+", " ", b6)
        b6 = b6.strip()
        b7 = list(punctuation)
        b8 = filter(lambda x: x not in b7 + [',', "â", '!', ':', "â"], b6)
        b9 = "".join(ch for ch in list(b8))
        b2.append(b9.lower())
b10 = load('model.bin')
b11 = b10.predict(b2)
with open('b12.txt', 'w+', b3 = 'utf-8') as f:
    for y in b11:
        b12 = {'classification': y}
        b13 = json.dumps(b12)
        f.write(b13 + "\n")
print(time.process_time() - b1, 'seconds')