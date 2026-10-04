import os
import pandas as pd
import distance
print('All modules imported correctly')
verbose = 0
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
output_file = 'document_similarity_levenstein_business.csv'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))][:3]
fileData = [' '.join(open(os.path.join(mypath, f), 'r').read().strip().split()[1:]) for f in onlyfiles]
new_df = pd.DataFrame()
for i, f1 in enumerate(fileData):
    for j, f2 in enumerate(fileData):
        if i <= j:
            new_df.loc[i, j] = distance.nlevenshtein(f1.lower().strip(), f2.lower().strip(), method=2)
            new_df.loc[j, i] = new_df.loc[i, j]
        if verbose and (j % 100 == 0):
            print('Currently processing', onlyfiles[i], 'with', onlyfiles[j])
new_df.columns = onlyfiles
new_df.index = onlyfiles
print('All calculations made. Exporting to csv')
new_df.to_csv(output_file, encoding='utf-8')
print('Export to csv done!')