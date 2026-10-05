import os
import pandas as pd
def get_file_list(directory):
    return os.listdir(directory)
def process_files(input_dir, output_dir):
    input_files = get_file_list(input_dir)
    output_files = get_file_list(output_dir)
    os.chdir(input_dir)
    for filename in input_files:
        if filename not in output_files:
            try:
                df = pd.read_csv(filename, sep='    ', header=None, engine='python')
                filtered_df = df[df[1] > 0]
                sorted_df = filtered_df.sort_values(by=1, ascending=False)
                top_50_rows = sorted_df.head(50)
                output_file_path = os.path.join(output_dir, filename.replace('.txt', '') + '.txt')
                top_50_rows.to_csv(output_file_path, sep='\t', header=None, index=False)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print('Processing completed!')
input_directory = '/TF-IDF'
output_directory = '/TF-IDF1'
process_files(input_directory, output_directory)