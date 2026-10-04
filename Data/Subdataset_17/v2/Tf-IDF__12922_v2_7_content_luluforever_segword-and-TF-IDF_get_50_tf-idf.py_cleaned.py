
import os
import pandas as pd
def get_file_list(directory):
    return os.listdir(directory)
def process_files(source_dir, target_dir):
    source_files = get_file_list(source_dir)
    target_files = get_file_list(target_dir)
    os.chdir(source_dir)
    error_count = 0
    for file_name in source_files:
        if file_name not in target_files:
            try:
                df = pd.read_csv(file_name, sep='    ', header=None, engine='python')
                filtered_df = df[df[1] > 0].sort_values(by=[1], ascending=False)
                if len(filtered_df) > 50:
                    filtered_df = filtered_df.iloc[:50]
                output_file_name = file_name.replace('.txt', '') + '.txt'
                output_path = os.path.join(target_dir, output_file_name)
                filtered_df.to_csv(output_path, sep='\t', header=None, index=False)
            except Exception as e:
                error_count += 1
                print(f"Error processing file {file_name}: {e}")
    print('Processing complete!')
    print(f'Total errors: {error_count}')
source_directory = '/TF-IDF'
target_directory = '/TF-IDF1'
process_files(source_directory, target_directory)