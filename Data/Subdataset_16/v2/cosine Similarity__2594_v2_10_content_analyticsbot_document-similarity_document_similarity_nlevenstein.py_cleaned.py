import os
import pandas as pd
import distance
print('All modules imported correctly')
a1 = 0
b1 = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
b2 = 'document_similarity_levenstein_business.csv'
b3 = [f for f in os.listdir(b1) if os.path.isfile(os.path.join(b1, f))][:3]
b4 = []
for file_name in b3:
    b5 = os.path.join(b1, file_name)
    with open(b5, 'r') as file:
        b6 = ' '.join(file.read().strip().split()[1:])
        b4.append(b6)
b7 = pd.DataFrame()
for i, content1 in enumerate(b4):
    for j, content2 in enumerate(b4):
        if i <= j:
            b8 = distance.nlevenshtein(content1.lower().strip(), content2.lower().strip(), method=2)
            b7.loc[i, j] = b8
            b7.loc[j, i] = b8
        if a1 and (j % b9 = = 0):
            print(f'Currently processing {b3[i]} with {b3[j]}')
b7.b10 = b3
b7.b11 = b3
print('All calculations made. Exporting to CSV')
b7.to_csv(b2, b12 = 'utf-8')
print('Export to CSV done!')