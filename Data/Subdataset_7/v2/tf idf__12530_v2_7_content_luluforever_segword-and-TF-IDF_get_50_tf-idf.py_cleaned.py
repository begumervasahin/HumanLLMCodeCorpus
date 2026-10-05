import os
import pandas as pd
def fonk1(directory):
    b1 = os.listdir(directory)
    return b1
def fonk2(input_dir, output_dir):
    b2 = fonk1(input_dir)
    b3 = fonk1(output_dir)
    os.chdir(input_dir)
    for filename in b2:
        if filename not in b3:
            try:
                b4 = pd.read_csv(filename, b9='    ', header=None, engine='python')
                b5 = b4[b4[1] > 0]
                b6 = b5.sort_values(by=1, axis=0, ascending=False)
                b7 = b6.head(50)
                b8 = os.path.join(output_dir, filename.replace('.txt', '') + '.txt')
                b7.to_csv(b8, b9 = '\t', header=None, index=False)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print('Processing completed!')
b10 = '/TF-IDF'
b11 = '/TF-IDF1'
fonk2(b10, b11)