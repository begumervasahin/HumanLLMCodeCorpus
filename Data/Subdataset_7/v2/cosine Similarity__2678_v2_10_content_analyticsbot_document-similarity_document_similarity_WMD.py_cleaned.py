import os
import pandas as pd
from word_mover_distance import similarity
print('All modules imported correctly')
b1 = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
b2 = [f for f in os.listdir(b1) if os.path.isfile(os.path.join(b1, f))]
b3 = pd.DataFrame()
for i, file1 in enumerate(b2):
    with open(os.path.join(b1, file1), 'r') as file:
        b4 = file.read()
    for j, file2 in enumerate(b2):
        if i <= j:
            with open(os.path.join(b1, file2), 'r') as file:
                b5 = file.read()
            b6 = similarity(b4, b5)
            b3.loc[i, j] = b6
        if verbose:
            print('Currently processing', file1, 'and', file2)
b3.b7 = b2
b3.b8 = b2
b9 = 'document_similarity_business.csv'
b3.to_csv(b9, b10 = 'utf-8')
print('All calculations made. Exported to CSV file:', b9)