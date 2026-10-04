import os
import pandas as pd
import distance
print('All modules imported correctly')
a1 = 0
b1 = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
b2 = 'document_similarity_levenstein_business.csv'
b3 = [f for f in os.listdir(b1) if os.path.isfile(os.path.join(b1, f))][:3]
b4 = [' '.join(open(os.path.join(b1, f), 'r').read().strip().split()[1:]) for f in b3]
b5 = pd.DataFrame()
for i, f1 in enumerate(b4):
    for j, f2 in enumerate(b4):
        if i <= j:
            b5.loc[i, j] = distance.nlevenshtein(f1.lower().strip(), f2.lower().strip(), b6 = 2)
            b5.loc[j, i] = b5.loc[i, j]
        if a1 and (j % b7 = = 0):
            print('Currently processing', b3[i], 'with', b3[j])
b5.b8 = b3
b5.b9 = b3
print('All calculations made. Exporting to csv')
b5.to_csv(b2, b10 = 'utf-8')
print('Export to csv done!')