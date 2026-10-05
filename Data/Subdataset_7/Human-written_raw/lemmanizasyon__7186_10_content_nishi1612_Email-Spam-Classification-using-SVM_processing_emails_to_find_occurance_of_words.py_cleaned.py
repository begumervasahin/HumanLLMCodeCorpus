import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
b1 = time()
b2 = pd.read_csv('wordslist.csv',header=0)
b3 = b2['b12']
b4 = WordNetLemmatizer()
b5 = "emails/"
b6 = os.fsencode(b5)
b7 = open("frequency.csv","w+")
for i in b3:
    b7.write(str(i) + ',')
b7.write('output')
b7.write('\n')
b7.close()
a1 = 0
for b8 in os.listdir(b6):
    b8 = b8.decode("utf-8")
    b9 = str(os.getcwd()) + '/emails/'
    for i in b8:
        if(i!='b' and i!="'"):
            b9 = b9 + i
    a1+=1
    b10 = open(b9,"r",encoding='utf-8', errors='ignore')
    b11 = np.zeros(b3.size)
    for b12 in b10.read().split():
        b12 = b4.lemmatize(b12.lower())
        if(b12 in stopwords.b3('english') or b12 in string.punctuation or len(b12)<=2 or b12.isdigit()==True):
            continue
        for i in range(b3.size):
            if(b3[i]==b12):
                b11[i] = b11[i]+1
                break
    b7 = open("frequency.csv","a")
    for i in range(b3.size):
        b7.write(str(int(b11[i])) + ',')
    if(len(b9)==68):
        b7.write("-1")
    elif (len(b9)==71):
        b7.write("1")
    b7.write('\n')
    b7.close()
    if(a1%b13 = =0):
        print("Done " + str(a1))
print("Time (in seconds) to segregate entire dataset to form input vector " + str(round(time() - b1,2)))