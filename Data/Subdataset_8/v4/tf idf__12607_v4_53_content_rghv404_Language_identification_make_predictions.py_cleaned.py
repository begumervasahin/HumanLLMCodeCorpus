import re
import json
import time
from string import punctuation
from joblib import load
start_time = time.time()
cleaned_test_data = []
with open(r'..\test_X_languages_homework.json.txt') as file:
    for json_obj in file.readlines():
        feature = json.loads(json_obj, encoding='utf-8')
        text = feature['text']
        clean_text = re.sub(r"[-()\"]", "", text)
        clean_text = re.sub(r"\s+", " ", clean_text)
        clean_text = clean_text.strip()
        punc = list(punctuation)
        temp = filter(lambda char: char not in punc + [',', "â", '!', ':', "â"], clean_text)
        clean_text = "".join(char for char in list(temp))
        cleaned_test_data.append(clean_text.lower())
model = load(r'model.bin', 'r')
predicted_classes = model.predict(cleaned_test_data)
with open(r'predictions.txt', 'w+', encoding='utf-8') as file:
    for prediction in predicted_classes:
        prediction_dict = {'classification': prediction}
        json_obj = json.dumps(prediction_dict)
        file.write(json_obj + "\n")
print(time.time() - start_time, 'seconds')