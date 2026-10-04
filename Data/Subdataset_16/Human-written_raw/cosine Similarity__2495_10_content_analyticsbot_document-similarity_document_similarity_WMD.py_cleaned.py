import difflib
from os import listdir
from os.path import isfile, join
import pandas as pd
from word_mover_distance import similarity
import os
print 'all modules imported correctly'
a1 = 0
b1 = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
b2 = [f for f in listdir(b1) if isfile(join(b1, f))]
b3 = pd.DataFrame()
a2 = 0
for f1 in b2:
    print f1
    b4 = open(join(b1, f1), 'r').read()
    a3 = 0
    for f2 in b2:
        if a2<=a3:
            b5 = open(join(b1, f2), 'r').read()
            b3.loc[a2, a3] = similarity(b4, b5)
        if a1:
            print 'currently processing', a2, ', ', a3
        a3+=1
    a2+=1
b3.b6 = b2
b3.b7 = b2
print 'all calculations made. Exporting to csv'
b3.to_csv('document_similarity_business.csv', b8 = 'utf-8')
print 'Export to csv done!'