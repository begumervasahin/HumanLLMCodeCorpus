import re
import json
import time
from string import punctuation
from joblib import load
start_time = time.time()
x_test = []
with open(r'..\test_X_languages_homework.json.txt', 'r', encoding='utf-8') as f:
    objects = f.readlines()
    for j_obj in objects:
        feature = json.loads(j_obj)['text']
        feature_clean = re.sub(r"[-()\"
        feature_clean = re.sub(r"\s+", " ", feature_clean)
        feature_clean = feature_clean.strip()
        punc_to_remove = set(punctuation + ',â!:â')
        clean_text = ''.join(ch for ch in feature_clean if ch not in punc_to_remove)
        x_test.append(clean_text.lower())
pipe = load(r'model.bin')
y_predicted = pipe.predict(x_test)
with open(r'predictions.txt', 'w', encoding='utf-8') as f:
    for y in y_predicted:
        predictions = {'classification': y}
        json_obj = json.dumps(predictions)
        f.write(json_obj + "\n")
print(f"{time.time() - start_time} seconds")