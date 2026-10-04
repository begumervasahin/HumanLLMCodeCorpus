
import os
import pandas as pd
def get_file_list(directory):
    return os.listdir(directory)
def process_files(source_dir, target_dir):
    all_files = get_file_list(source_dir)
    target_files = get_file_list(target_dir)
    os.chdir(source_dir)
    errors = 0
    for file in all_files:
        if file not in target_files:
            try:
                df = pd.read_csv(file, sep='    ', header=None, engine='python')
                df_filtered = df[df[1] > 0].sort_values(by=[1], ascending=False)
                if len(df_filtered) <= 50:
                    df_to_save = df_filtered
                else:
                    df_to_save = df_filtered.iloc[:50]
                filename = file.replace('.txt', '')
                target_path = os.path.join(target_dir, f'{filename}.txt')
                df_to_save.to_csv(target_path, sep='\t', header=None, index=False)
            except Exception as e:
                errors += 1
                print(f"Error processing file {file}: {e}")
    print('Processing complete!')
    print(f'Total errors: {errors}')
source_directory = '/TF-IDF'
target_directory = '/TF-IDF1'
process_files(source_directory, target_directory)