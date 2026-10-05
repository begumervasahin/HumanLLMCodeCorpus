import os
import pandas as pd
import distance
print('All modules imported correctly')
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))][:3]
file_data = []
for filename in onlyfiles:
    with open(os.path.join(mypath, filename), 'r') as file:
        content = file.read().strip().split()[1:]
        file_data.append(' '.join(content))
similarity_df = pd.DataFrame()
for i, text1 in enumerate(file_data):
    text1_lower = text1.lower().strip()
    for j, text2 in enumerate(file_data):
        if i <= j:
            text2_lower = text2.lower().strip()
            similarity_score = distance.nlevenshtein(text1_lower, text2_lower, method=2)
            similarity_df.loc[i, j] = similarity_score
similarity_df.columns = onlyfiles
similarity_df.index = onlyfiles
csv_filename = 'document_similarity_levenstein_business.csv'
similarity_df.to_csv(csv_filename, encoding='utf-8')
print('All calculations made. Exported to CSV file:', csv_filename)