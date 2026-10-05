import os
import pandas as pd
import distance
print('All modules imported correctly')
a1 = 0
b1 = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
b2 = [f for f in os.listdir(b1) if os.path.isfile(os.path.join(b1, f))][:3]
b3 = []
for file_name in b2:
    with open(os.path.join(b1, file_name), 'r') as file:
        b4 = file.read().strip().split()[1:]
        b3.append(' '.join(b4))
b5 = pd.DataFrame()
for i, f1 in enumerate(b3):
    b6 = f1.lower().strip()
    for j, f2 in enumerate(b3):
        if i <= j:
            b5.loc[i, j] = distance.nlevenshtein(b6, f2.lower().strip(), b7 = 2)
        if a1 and (j % b8 = = 0):
            print('Currently processing', b2[i], 'with', b2[j])
b5.b9 = b2
b5.b10 = b2
b11 = 'document_similarity_levenstein_business.csv'
b5.to_csv(b11, b12 = 'utf-8')
print('All calculations made. Exported to CSV file:', b11)