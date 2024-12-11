
import os
import pandas as pd
def fonk1(directory):
    b1 = directory
    b2 = []
    b3 = os.listdir(b1)
    for file in b3:
        b2.append(file)
    return b2
b4 = fonk1('/TF-IDF')
b5 = fonk1('/TF-IDF1')
os.chdir('/TF-IDF')
b1 = '/TF-IDF1'
a1 = 0
for filename in b4:
    if filename not in b5:
        try:
            b6 = pd.read_csv(filename, b11='    ', header=None, engine='python')
            b7 = b6[b6[1] > 0]
            b8 = b7.sort_values(by=[1], axis=0, ascending=False)
            if len(b8) <= 50:
                b9 = filename.replace('.txt', '')
                b10 = b1 + '/' + b9 + '.txt'
                b8.to_csv(b10, b11 = '\t', header=None, index=False)
            else:
                b12 = b8.iloc[0:50, :]
                b9 = filename.replace('.txt', '')
                b10 = b1 + '/' + b9 + '.txt'
                b12.to_csv(b10, b11 = '\t', header=None, index=False)
        except Exception as e:
            a1 += 1
print('Execution complete!')