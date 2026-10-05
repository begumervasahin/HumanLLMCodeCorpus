import os
import pandas as pd
import distance
print('All modules imported correctly')
verbose = 0
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))][:3]
file_data = []
for file_name in onlyfiles:
    with open(os.path.join(mypath, file_name), 'r') as file:
        file_content = file.read().strip().split()[1:]
        file_data.append(' '.join(file_content))
new_df = pd.DataFrame()
for i, f1 in enumerate(file_data):
    s1 = f1.lower().strip()
    for j, f2 in enumerate(file_data):
        if i <= j:
            new_df.loc[i, j] = distance.nlevenshtein(s1, f2.lower().strip(), method=2)
        if verbose and (j % 100 == 0):
            print('Currently processing', onlyfiles[i], 'with', onlyfiles[j])
new_df.columns = onlyfiles
new_df.index = onlyfiles
csv_filename = 'document_similarity_levenstein_business.csv'
new_df.to_csv(csv_filename, encoding='utf-8')
print('All calculations made. Exported to CSV file:', csv_filename)