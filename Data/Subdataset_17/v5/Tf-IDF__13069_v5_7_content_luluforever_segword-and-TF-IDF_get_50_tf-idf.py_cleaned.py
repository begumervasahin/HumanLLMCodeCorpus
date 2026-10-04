import os
import pandas as pd
def get_file_list(directory):
    return os.listdir(directory)
def process_file(file, target_dir):
    try:
        df = pd.read_csv(file, sep='    ', header=None, engine='python')
        filtered_df = df[df[1] > 0].sort_values(by=[1], ascending=False)
        output_df = filtered_df if len(filtered_df) <= 50 else filtered_df.iloc[:50, :]
        output_filename = file.replace('.txt', '')
        output_path = os.path.join(target_dir, f"{output_filename}.txt")
        output_df.to_csv(output_path, sep='\t', header=None, index=False)
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return False
    return True
def process_files(source_dir, target_dir):
    source_files = get_file_list(source_dir)
    target_files = get_file_list(target_dir)
    os.chdir(source_dir)
    skipped_files_count = 0
    for file in source_files:
        if file not in target_files:
            success = process_file(file, target_dir)
            if not success:
                skipped_files_count += 1
    print(f"Processing completed with {skipped_files_count} files skipped due to errors.")
if __name__ == "__main__":
    source_directory = '/TF-IDF'
    target_directory = '/TF-IDF1'
    process_files(source_directory, target_directory)