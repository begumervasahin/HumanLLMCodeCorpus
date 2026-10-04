import os
import pandas as pd
import re
ENCODING = 'utf-8'
def load_data_from_directory(directory_path):
    data = []
    txt_files = [file for file in os.listdir(directory_path)
                 if os.path.isfile(os.path.join(directory_path, file)) and file.endswith(".txt")]
    for txt_file in txt_files:
        file_path = os.path.join(directory_path, txt_file)
        data.extend(read_file_content(file_path))
    processed_data = [process_data(item) for item in data]
    return processed_data
def read_file_content(file_path):
    with open(file_path, "r", encoding=ENCODING) as file:
        return file.read().split('\n')
def process_data(data):
    pattern = r"[0-9]+"
    number_strings = re.findall(pattern, data)
    numbers = [float(num_str) for num_str in number_strings]
    return numbers[:3]
def save_data_to_csv(data, csv_file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(csv_file_path, index=False, encoding=ENCODING)
