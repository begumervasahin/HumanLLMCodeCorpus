import os
import pandas as pd
def fonk1(directory):
    return os.listdir(directory)
def fonk2(file, target_dir):
    try:
        b1 = pd.read_csv(file, b6='    ', header=None, engine='python')
        b2 = b1[b1[1] > 0].sort_values(by=[1], ascending=False)
        b3 = b2 if len(b2) <= 50 else b2.iloc[:50, :]
        b4 = file.replace('.txt', '')
        b5 = os.path.join(target_dir, f"{b4}.txt")
        b3.to_csv(b5, b6 = '\t', header=None, index=False)
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return False
    return True
def fonk3(source_dir, target_dir):
    b7 = fonk1(source_dir)
    b8 = fonk1(target_dir)
    os.chdir(source_dir)
    a1 = 0
    for file in b7:
        if file not in b8:
            b9 = fonk2(file, target_dir)
            if not b9:
                a1 += 1
    print(f"Processing completed with {a1} files skipped due to errors.")
if b10 = = "__main__":
    b11 = '/TF-IDF'
    b12 = '/TF-IDF1'
    fonk3(b11, b12)