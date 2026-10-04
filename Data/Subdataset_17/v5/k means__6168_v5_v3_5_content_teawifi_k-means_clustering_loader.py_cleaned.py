import os
import re
import pandas as pd
ENCODING = 'utf-8'
def load_data(directory):
    data = []
    text_files = [file for file in os.listdir(directory) if file.endswith(".txt")]
    for file in text_files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding=ENCODING) as f:
                lines = f.readlines()
                data.extend(lines)
    filtered_data = [extract_numerical_values(line) for line in data]
    return filtered_data
def extract_numerical_values(text):
    pattern = r"[0-9]+"
    numbers = [float(num) for num in re.findall(pattern, text)]
    return numbers[:3]
def save_to_csv(data, file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(file_path, index=False, encoding=ENCODING)
if __name__ == "__main__":
    data_directory = "/path/to/directory"
    output_file = "output.csv"
    data = load_data(data_directory)
    save_to_csv(data, output_file)