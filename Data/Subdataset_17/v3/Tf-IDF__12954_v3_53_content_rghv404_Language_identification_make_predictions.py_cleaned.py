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
    cleaned_text = ''.join(char for char in text if char not in punc)
    return cleaned_text.lower()
def read_and_clean_data(file_path):
    x_test = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            feature = json.loads(line)
            feature_text = feature.get('text', '')
            cleaned_text = clean_text(feature_text)
            x_test.append(cleaned_text)
    return x_test
def write_predictions(predictions, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for prediction in predictions:
            predictions_dict = {'classification': prediction}
            json_obj = json.dumps(predictions_dict)
            file.write(json_obj + "\n")
def main():
    start_time = time.time()
    input_file_path = r'..\test_X_languages_homework.json.txt'
    output_file_path = r'predictions.txt'
    model_path = r'model.bin'
    x_test = read_and_clean_data(input_file_path)
    model = load(model_path)
    y_predicted = model.predict(x_test)
    write_predictions(y_predicted, output_file_path)
    elapsed_time = time.time() - start_time
    print(f"Execution Time: {elapsed_time:.2f} seconds")
if __name__ == "__main__":
    main()