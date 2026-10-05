import os
import pandas as pd
def getFilelist(directory):
    filelist = os.listdir(directory)
    return filelist
def process_files(input_dir, output_dir):
    allfile = getFilelist(input_dir)
    allfile1 = getFilelist(output_dir)
    os.chdir(input_dir)
    for filename in allfile:
        if filename not in allfile1:
            try:
                df = pd.read_csv(filename, sep='    ', header=None, engine='python')
                df_filtered = df[df[1] > 0]
                df_sorted = df_filtered.sort_values(by=1, axis=0, ascending=False)
                df_top_50 = df_sorted.head(50)
                output_file = os.path.join(output_dir, filename.replace('.txt', '') + '.txt')
                df_top_50.to_csv(output_file, sep='\t', header=None, index=False)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print('Execution completed!')
input_directory = '/TF-IDF'
output_directory = '/TF-IDF1'
process_files(input_directory, output_directory)