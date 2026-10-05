import difflib
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from word_mover_distance import similarity
print('All modules imported correctly')
mypath = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
new_df = pd.DataFrame()
for i, file1 in enumerate(onlyfiles):
    s1 = open(join(mypath, file1), 'r').read()
    for j, file2 in enumerate(onlyfiles):
        if i <= j:
            s2 = open(join(mypath, file2), 'r').read()
            new_df.loc[i, j] = similarity(s1, s2)
        if verbose:
            print('Currently processing', file1, 'and', file2)
new_df.columns = onlyfiles
new_df.index = onlyfiles
csv_filename = 'document_similarity_business.csv'
new_df.to_csv(csv_filename, encoding='utf-8')
print('All calculations made. Exported to CSV file:', csv_filename)