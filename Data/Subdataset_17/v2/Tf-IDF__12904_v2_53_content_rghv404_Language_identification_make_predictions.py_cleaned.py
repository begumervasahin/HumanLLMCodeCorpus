import re
import json
import time
from string import punctuation
from joblib import load
def clean_text(text):
    text = re.sub(r"[-()\"
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    punc = set(punctuation) | {',', "â", '!', ':', "â"}
    clean_text = ''.join(char for char in text if char not in punc)
    return clean_text.lower()
def main():
    start_time = time.time()
    x_test = []
    with open(r'..\test_X_languages_homework.json.txt', 'r', encoding='utf-8') as file:
        for line in file:
            feature = json.loads(line)
            feature_text = feature.get('text', '')
            cleaned_text = clean_text(feature_text)
            x_test.append(cleaned_text)
    pipe = load(r'model.bin')
    y_predicted = pipe.predict(x_test)
    with open(r'predictions.txt', 'w', encoding='utf-8') as file:
        for prediction in y_predicted:
            predictions = {'classification': prediction}
            json_obj = json.dumps(predictions)
            file.write(json_obj + "\n")
    elapsed_time = time.time() - start_time
    print(f"{elapsed_time:.2f} seconds")
if __name__ == "__main__":
    main()