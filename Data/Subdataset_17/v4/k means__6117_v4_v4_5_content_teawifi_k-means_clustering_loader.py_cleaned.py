import os
import pandas as pd
import re
from settings import ENCODING
def load_data(path_to_dir):
    data = []
    txt_files = [file for file in os.listdir(path_to_dir)
                 if os.path.isfile(os.path.join(path_to_dir, file)) and file.endswith(".txt")]
    for file in txt_files:
        with open(os.path.join(path_to_dir, file), "r", encoding=ENCODING) as f:
            lines = f.read().splitlines()
            for line in lines:
                filtered_data = filter_data(line)
                if filtered_data:
                    data.append(filtered_data)
    return data
def filter_data(data):
    pattern = r"\d+(\.\d+)?"
    matches = re.findall(pattern, data)
    numbers = [float(num) for num in matches]
    return numbers[:3]
def save_to_csv(data, file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(file_path, index=False, encoding=ENCODING)
