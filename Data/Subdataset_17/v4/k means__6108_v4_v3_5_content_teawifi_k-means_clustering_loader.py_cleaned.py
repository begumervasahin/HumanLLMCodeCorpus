import os
import re
import pandas as pd
ENCODING = 'utf-8'
def load_data(path_to_dir):
    data = []
    files = [file for file in os.listdir(path_to_dir) if file.endswith(".txt")]
    for file in files:
        file_path = os.path.join(path_to_dir, file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding=ENCODING) as f:
                content = f.read().split('\n')
                data.extend(content)
    filtered_data = [filter_data(item) for item in data]
    return filtered_data
def filter_data(data):
    pattern = r"[0-9]+"
    numbers = [float(num) for num in re.findall(pattern, data)]
    return numbers[:3]
def save_to_csv(data, file_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(file_path, index=False, encoding=ENCODING)
if __name__ == "__main__":
    data_directory = "/path/to/directory"
    output_file = "output.csv"
    data = load_data(data_directory)
    save_to_csv(data, output_file)