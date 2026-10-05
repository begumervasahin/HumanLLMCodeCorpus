import os
import pandas as pd
def get_file_list(directory):
    path = directory
    files = os.listdir(path)
    return files
all_files_original = get_file_list('/TF-IDF')
all_files_modified = get_file_list('/TF-IDF1')
os.chdir('/TF-IDF')
destination_path = '/TF-IDF1'
exception_count = 0
for file_name in all_files_original:
    if file_name not in all_files_modified:
        try:
            data = pd.read_csv(file_name, sep='    ', header=None, engine='python')
            filtered_data = data[data[1] > 0]
            sorted_data = filtered_data.sort_values(by=[1], axis=0, ascending=False)
            if len(sorted_data) <= 50:
                new_file_name = file_name.replace('.txt', '')
                new_file_path = f"{destination_path}/{new_file_name}.txt"
                sorted_data.to_csv(new_file_path, sep='\t', header=None, index=False)
            else:
                top_50 = sorted_data.iloc[0:50, :]
                new_file_name = file_name.replace('.txt', '')
                new_file_path = f"{destination_path}/{new_file_name}.txt"
                top_50.to_csv(new_file_path, sep='\t', header=None, index=False)
        except Exception as e:
            exception_count += 1
print('Execution complete!')