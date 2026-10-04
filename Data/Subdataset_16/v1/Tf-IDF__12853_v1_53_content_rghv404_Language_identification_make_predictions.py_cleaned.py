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
        b5 = json.loads(j_obj)
        b6 = b5['text']
        b7 = re.sub(r"[-()\"
        b7 = re.sub(r"\s+", " ", b7)
        b7 = b7.strip()
        b8 = list(punctuation) + [',', "â", '!', ':', "â"]
        b9 = filter(lambda x: x not in b8, b7)
        b10 = "".join(b9)
        b2.append(b10.lower())
b11 = load(r'model.bin')
b12 = b11.predict(b2)
with open(r'b13.txt', 'w+', b3 = 'utf-8') as f:
    for y in b12:
        b13 = {'classification': y}
        b14 = json.dumps(b13)
        f.write(b14 + "\n")
print(time.time() - b1, 'seconds')