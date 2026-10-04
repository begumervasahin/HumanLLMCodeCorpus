import os
import pandas as pd
from word_mover_distance import similarity
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(b9, file_path, b1 = 0):
    b2 = len(b9)
    b3 = pd.DataFrame(b12=range(b2), b11=range(b2))
    for i, file1 in enumerate(b9):
        print(file1)
        b4 = fonk1(os.path.join(file_path, file1))
        for j, file2 in enumerate(b9):
            if i <= j:
                b5 = fonk1(os.path.join(file_path, file2))
                b6 = similarity(b4, b5)
                b3.loc[i, j] = b6
                b3.loc[j, i] = b6
            if b1:
                print(f'Currently processing {i}, {j}')
    return b3
def fonk3():
    print('All modules imported correctly')
    b1 = 0
    b7 = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
    b8 = 'document_similarity_business.csv'
    b9 = [f for f in os.listdir(b7) if os.path.isfile(os.path.join(b7, f))]
    b10 = fonk2(b9, b7, b1)
    b10.b11 = b9
    b10.b12 = b9
    print('All calculations made. Exporting to CSV')
    b10.to_csv(b8, b13 = 'utf-8')
    print('Export to CSV done!')
if b14 = = "__main__":
    fonk3()