import os
import re
import pandas as pd
ENCODING = 'utf-8'
def load_data_from_directory(directory_path):
    data = []
    txt_files = [file for file in os.listdir(directory_path) if file.endswith(".txt")]
    for txt_file in txt_files:
        file_path = os.path.join(directory_path, txt_file)
        with open(file_path, "r", encoding=ENCODING) as file:
            lines = file.readlines()
            data.extend(lines)
    filtered_data = [extract_numerical_values(line) for line in data]
    return filtered_data
def extract_numerical_values(text):
    pattern = r"[0-9]+"
    matches = re.findall(pattern, text)
    numbers = [float(num) for num in matches]
    return numbers[:3]
def save_data_to_csv(data, output_path):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    df.to_csv(output_path, index=False, encoding=ENCODING)
def main():
    data_directory = "/path/to/directory"
    output_file = "output.csv"
    filtered_data = load_data_from_directory(data_directory)
    save_data_to_csv(filtered_data, output_file)
if __name__ == "__main__":
    main()