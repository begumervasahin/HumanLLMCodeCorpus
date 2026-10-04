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
        feature = json.loads(j_obj)
        feature_text = feature['text']
        feature_clean = re.sub(r"[-()\"
        feature_clean = re.sub(r"\s+", " ", feature_clean)
        feature_clean = feature_clean.strip()
        punc = list(punctuation) + [',', "â", '!', ':', "â"]
        temp = filter(lambda x: x not in punc, feature_clean)
        clean_text = "".join(temp)
        x_test.append(clean_text.lower())
pipe = load(r'model.bin')
y_predicted = pipe.predict(x_test)
with open(r'predictions.txt', 'w+', encoding='utf-8') as f:
    for y in y_predicted:
        predictions = {'classification': y}
        json_obj = json.dumps(predictions)
        f.write(json_obj + "\n")
print(time.time() - start_time, 'seconds')