import os
import pandas as pd
def fonk1(directory):
    return os.listdir(directory)
def fonk2(source_dir, target_dir):
    b1 = fonk1(source_dir)
    b2 = fonk1(target_dir)
    os.chdir(source_dir)
    a1 = 0
    for file in b1:
        if file not in b2:
            try:
                b3 = pd.read_csv(file, b8='    ', header=None, engine='python')
                b4 = b3[b3[1] > 0].sort_values(by=[1], ascending=False)
                b5 = b4 if len(b4) <= 50 else b4.iloc[:50, :]
                b6 = file.replace('.txt', '')
                b7 = os.path.join(target_dir, f"{b6}.txt")
                b5.to_csv(b7, b8 = '\t', header=None, index=False)
            except Exception as e:
                a1 += 1
    print(f"Processing completed with {a1} files skipped due to errors.")
if b9 = = "__main__":
    b10 = '/TF-IDF'
    b11 = '/TF-IDF1'
    fonk2(b10, b11)