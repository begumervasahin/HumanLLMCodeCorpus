import re, json, time
from string import punctuation
from joblib import load
b1 = time.clock()
b2 = []
with open(r'..\test_X_languages_homework.json.txt') as f:
    b3 = f.readlines()
    for j_obj in b3:
        b4 = json.loads(j_obj, b11='utf-8')
        b4 = b4['text']
        b5 = re.sub(r"[-()\"
        b5 = re.sub(r"\s+", " ", b5)
        b5 = b5.strip()
        b6 = list(punctuation)
        b7 = filter(lambda x: x not in b6 + [',', "â", '!', ':', "â"], b5)
        b8 = "".join(ch for ch in list(b7))
        b2.append(b8.lower())
b9 = load(r'model.bin', 'r')
b10 = b9.predict(b2)
with open(r'b12.txt', 'w+', b11 = 'utf-8') as f:
    for y in b10:
        b12 = dict()
        b12['classification'] = y
        b13 = json.dumps(b12)
        f.write(b13 + "\n")
print(time.clock() - b1, 'seconds')