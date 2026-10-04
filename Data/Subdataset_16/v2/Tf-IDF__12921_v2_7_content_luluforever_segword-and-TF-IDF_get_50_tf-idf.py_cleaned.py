
import os
import pandas as pd
def fonk1(directory):
    return os.listdir(directory)
def fonk2(source_dir, target_dir):
    b1 = fonk1(source_dir)
    b2 = fonk1(target_dir)
    os.chdir(source_dir)
    a1 = 0
    for file_name in b1:
        if file_name not in b2:
            try:
                b3 = pd.read_csv(file_name, b7='    ', header=None, engine='python')
                b4 = b3[b3[1] > 0].sort_values(by=[1], ascending=False)
                if len(b4) > 50:
                    b4 = b4.iloc[:50]
                b5 = file_name.replace('.txt', '') + '.txt'
                b6 = os.path.join(target_dir, b5)
                b4.to_csv(b6, b7 = '\t', header=None, index=False)
            except Exception as e:
                a1 += 1
                print(f"Error processing file {file_name}: {e}")
    print('Processing complete!')
    print(f'Total errors: {a1}')
b8 = '/TF-IDF'
b9 = '/TF-IDF1'
fonk2(b8, b9)