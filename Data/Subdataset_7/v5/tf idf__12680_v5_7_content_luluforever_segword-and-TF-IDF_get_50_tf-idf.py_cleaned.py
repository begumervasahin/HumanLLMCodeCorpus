import os
import pandas as pd
def fonk1(directory):
    b1 = directory
    b2 = os.listdir(b1)
    return b2
b3 = fonk1('/TF-IDF')
b4 = fonk1('/TF-IDF1')
os.chdir('/TF-IDF')
b5 = '/TF-IDF1'
a1 = 0
for file_name in b3:
    if file_name not in b4:
        try:
            b6 = pd.read_csv(file_name, b11='    ', header=None, engine='python')
            b7 = b6[b6[1] > 0]
            b8 = b7.sort_values(by=[1], axis=0, ascending=False)
            if len(b8) <= 50:
                b9 = file_name.replace('.txt', '')
                b10 = f"{b5}/{b9}.txt"
                b8.to_csv(b10, b11 = '\t', header=None, index=False)
            else:
                b12 = b8.iloc[0:50, :]
                b9 = file_name.replace('.txt', '')
                b10 = f"{b5}/{b9}.txt"
                b12.to_csv(b10, b11 = '\t', header=None, index=False)
        except Exception as e:
            a1 += 1
print('Execution complete!')