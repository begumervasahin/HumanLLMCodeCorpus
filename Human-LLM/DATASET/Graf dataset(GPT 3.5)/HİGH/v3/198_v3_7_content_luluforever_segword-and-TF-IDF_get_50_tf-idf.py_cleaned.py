import os
import pandas as pd
def fonk1(directory):
    return os.listdir(directory)
def fonk2(input_dir, output_dir):
    b1 = fonk1(input_dir)
    b2 = fonk1(output_dir)
    os.chdir(input_dir)
    for filename in b1:
        if filename not in b2:
            try:
                b3 = pd.read_csv(filename, b8='    ', header=None, engine='python')
                b4 = b3[b3[1] > 0]
                b5 = b4.sort_values(by=1, ascending=False)
                b6 = b5.head(50)
                b7 = os.path.join(output_dir, filename.replace('.txt', '') + '.txt')
                b6.to_csv(b7, b8 = '\t', header=None, index=False)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print('Processing completed!')
b9 = '/TF-IDF'
b10 = '/TF-IDF1'
fonk2(b9, b10)