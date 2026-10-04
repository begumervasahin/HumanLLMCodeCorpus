import os
import pandas as pd
import re
ENCODING = 'utf-8'
def load_data(path_to_dir):
    text_files = _get_text_files(path_to_dir)
    all_data = []
    for file in text_files:
        file_path = os.path.join(path_to_dir, file)
        file_content = _read_file_content(file_path)
        all_data.extend(file_content)
    filtered_data = [_extract_numbers(line) for line in all_data]
    return filtered_data
def _get_text_files(directory):
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file)) and file.endswith(".txt")
    ]
def _read_file_content(file_path):
    with open(file_path, "r", encoding=ENCODING) as file:
        return file.read().splitlines()
def _extract_numbers(text):
    pattern = r"[0-9]+"
    matches = re.findall(pattern, text)
    numbers = [float(match) for match in matches[:3]]
    return numbers
def save_to_csv(data, file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(file_path, index=False, encoding=ENCODING)
