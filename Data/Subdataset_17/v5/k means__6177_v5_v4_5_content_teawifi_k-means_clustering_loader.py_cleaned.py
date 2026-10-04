import os
import pandas as pd
import re
from settings import ENCODING
def load_data(directory_path):
    data = []
    txt_files = [file for file in os.listdir(directory_path)
                 if file.endswith(".txt") and os.path.isfile(os.path.join(directory_path, file))]
    for file in txt_files:
        file_path = os.path.join(directory_path, file)
        with open(file_path, "r", encoding=ENCODING) as f:
            lines = f.read().splitlines()
            for line in lines:
                filtered_numbers = extract_numbers(line)
                if filtered_numbers:
                    data.append(filtered_numbers)
    return data
def extract_numbers(text):
    pattern = r"\d+(\.\d+)?"
    matches = re.findall(pattern, text)
    numbers = [float(match) for match in matches]
    return numbers[:3]
def save_to_csv(data, output_file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(output_file_path, index=False, encoding=ENCODING)
