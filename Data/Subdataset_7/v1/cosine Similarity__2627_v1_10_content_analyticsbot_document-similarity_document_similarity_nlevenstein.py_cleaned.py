import os
import pandas as pd
import distance
print('All modules imported correctly')
a1 = 0
b1 = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
b2 = [f for f in os.listdir(b1) if os.path.isfile(os.path.join(b1, f))][:3]
b3 = [' '.join(open(os.path.join(b1, f), 'r').read().strip().split()[1:]) for f in b2]
b4 = pd.DataFrame()
a2 = 0
for f1 in b3:
    b5 = f1.lower().strip()
    a3 = 0
    for f2 in b3:
        if a2 <= a3:
            b4.loc[a2, a3] = distance.nlevenshtein(b5, f2.lower().strip(), b6 = 2)
        if a1 and (a3 % b7 = = 0):
            print('Currently processing', b2[a2], ' with ', b2[a3])
        a3 += 1
    a2 += 1
b4.b8 = b2
b4.b9 = b2
print('All calculations made. Exporting to CSV')
b4.to_csv('document_similarity_levenstein_business.csv', b10 = 'utf-8')
print('Export to CSV done!')