import os
import pandas as pd
import distance
print('All modules imported correctly')
verbose = 0
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
output_file = 'document_similarity_levenstein_business.csv'
file_list = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))][:3]
file_contents = []
for file_name in file_list:
    file_path = os.path.join(mypath, file_name)
    with open(file_path, 'r') as file:
        content = ' '.join(file.read().strip().split()[1:])
        file_contents.append(content)
similarity_df = pd.DataFrame()
for i, content1 in enumerate(file_contents):
    for j, content2 in enumerate(file_contents):
        if i <= j:
            distance_value = distance.nlevenshtein(content1.lower().strip(), content2.lower().strip(), method=2)
            similarity_df.loc[i, j] = distance_value
            similarity_df.loc[j, i] = distance_value
        if verbose and (j % 100 == 0):
            print(f'Currently processing {file_list[i]} with {file_list[j]}')
similarity_df.columns = file_list
similarity_df.index = file_list
print('All calculations made. Exporting to CSV')
similarity_df.to_csv(output_file, encoding='utf-8')
print('Export to CSV done!')