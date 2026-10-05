import os
import pandas as pd
from word_mover_distance import similarity
print('All modules imported correctly')
mypath = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
similarity_df = pd.DataFrame()
for i, file1 in enumerate(onlyfiles):
    with open(os.path.join(mypath, file1), 'r') as file1_handle:
        content1 = file1_handle.read()
    for j, file2 in enumerate(onlyfiles):
        if i <= j:
            with open(os.path.join(mypath, file2), 'r') as file2_handle:
                content2 = file2_handle.read()
            similarity_score = similarity(content1, content2)
            similarity_df.loc[i, j] = similarity_score
        if verbose:
            print('Currently processing:', file1, 'and', file2)
similarity_df.columns = onlyfiles
similarity_df.index = onlyfiles
csv_filename = 'document_similarity_business.csv'
similarity_df.to_csv(csv_filename, encoding='utf-8')
print('All calculations made. Exported to CSV file:', csv_filename)