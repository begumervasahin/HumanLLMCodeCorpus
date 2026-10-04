import re
import json
import time
from string import punctuation
from joblib import load
def load_and_clean_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cleaned_data = [clean_text(json.loads(line)['text']) for line in lines]
    return cleaned_data
def clean_text(text):
    text = re.sub(r"[-()\"
    text = re.sub(r"\s+", " ", text).strip()
    punc_to_remove = set(punctuation + ',â!:â')
    cleaned_text = ''.join(char for char in text if char not in punc_to_remove)
    return cleaned_text.lower()
def save_predictions(predictions, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for prediction in predictions:
            json_obj = json.dumps({'classification': prediction})
            file.write(json_obj + "\n")
def main():
    start_time = time.time()
    test_data_path = r'..\test_X_languages_homework.json.txt'
    x_test = load_and_clean_data(test_data_path)
    model_path = r'model.bin'
    model = load(model_path)
    y_predicted = model.predict(x_test)
    predictions_path = r'predictions.txt'
    save_predictions(y_predicted, predictions_path)
    print(f"{time.time() - start_time} seconds")
if __name__ == "__main__":
    main()