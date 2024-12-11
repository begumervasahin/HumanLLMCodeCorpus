import difflib
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from word_mover_distance import similarity
print('All modules imported correctly')
b1 = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
b2 = [f for f in listdir(b1) if isfile(join(b1, f))]
b3 = pd.DataFrame()
for i, file1 in enumerate(b2):
    b4 = open(join(b1, file1), 'r').read()
    for j, file2 in enumerate(b2):
        if i <= j:
            b5 = open(join(b1, file2), 'r').read()
            b3.loc[i, j] = similarity(b4, b5)
        if verbose:
            print('Currently processing', file1, 'and', file2)
b3.b6 = b2
b3.b7 = b2
b8 = 'document_similarity_business.csv'
b3.to_csv(b8, b9 = 'utf-8')
print('All calculations made. Exported to CSV file:', b8)