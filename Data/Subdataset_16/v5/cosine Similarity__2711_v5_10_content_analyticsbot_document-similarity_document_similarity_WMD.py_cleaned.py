import os
import pandas as pd
from word_mover_distance import similarity
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(b8, b6, b1 = 0):
    b2 = pd.DataFrame(index=b8, columns=b8)
    for i, file1 in enumerate(b8):
        print(f'Processing file: {file1}')
        b3 = fonk1(os.path.join(b6, file1))
        for j, file2 in enumerate(b8):
            if i <= j:
                b4 = fonk1(os.path.join(b6, file2))
                b5 = similarity(b3, b4)
                b2.loc[file1, file2] = b5
                b2.loc[file2, file1] = b5
            if b1:
                print(f'Currently processing {file1} with {file2}')
    return b2
def fonk3():
    print('All modules imported correctly')
    b1 = 0
    b6 = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
    b7 = 'document_similarity_business.csv'
    b8 = [f for f in os.listdir(b6) if os.path.isfile(os.path.join(b6, f))]
    b9 = fonk2(b8, b6, b1)
    print('All calculations made. Exporting to CSV')
    b9.to_csv(b7, b10 = 'utf-8')
    print('Export to CSV done!')
if b11 = = "__main__":
    fonk3()