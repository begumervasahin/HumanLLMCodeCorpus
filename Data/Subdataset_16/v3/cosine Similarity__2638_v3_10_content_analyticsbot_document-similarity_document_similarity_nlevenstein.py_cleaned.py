import os
import pandas as pd
import distance
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = ' '.join(file.read().strip().split()[1:])
    return b1
def fonk2(b9):
    b2 = len(b9)
    b3 = pd.DataFrame(b12=range(b2), b11=range(b2))
    for i, content1 in enumerate(b9):
        for j, content2 in enumerate(b9):
            if i <= j:
                b4 = distance.nlevenshtein(content1.lower().strip(), content2.lower().strip(), method=2)
                b3.iloc[i, j] = b4
                b3.iloc[j, i] = b4
            if a1 and (j % b5 = = 0):
                print(f'Currently processing file {i+1} with file {j+1}')
    return b3
def fonk3():
    print('All modules imported correctly')
    a1 = 0
    b6 = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
    b7 = 'document_similarity_levenstein_business.csv'
    b8 = [f for f in os.listdir(b6) if os.path.isfile(os.path.join(b6, f))][:3]
    b9 = [fonk1(os.path.join(b6, file_name)) for file_name in b8]
    b10 = fonk2(b9)
    b10.b11 = b8
    b10.b12 = b8
    print('All calculations made. Exporting to CSV')
    b10.to_csv(b7, b13 = 'utf-8')
    print('Export to CSV done!')
if b14 = = "__main__":
    fonk3()