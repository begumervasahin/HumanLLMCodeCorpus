14. Repository: Dawlatly/Recommender-system
   File: apriori.py
   URL: https:
   Code Content:
import numpy as np
np.set_printoptions(b1 = np.inf)
import matplotlib.pyplot as plt
import pandas as pd
b2 = pd.read_csv('FYP.csv')
from apyori import apriori
b3 = b2.iloc[:, [5,10]].values
b3 = b3[b3[:,0].argsort()]
b4 = []
b4.append([str('Labels')])
for b5 in range(0,9426):
    if(b5 = =0):
        continue
    if(b3[b5][0]==b3[b5-1][0]):
        b4[-1].append(str(b3[b5][1]))
    else:
        b4[-1]=list(set(b4[-1]))
        b4.append([str(b3[b5][1])])
b6 = apriori(b4, min_support=0.02,min_confidence=0.2,min_lift=1.4,min_length=2)
b7 = list(b6)
def fonk1(b7):
    b8 = [tuple(result[2][0][0]) for result in b7]
    b9 = [tuple(result[2][0][1]) for result in b7]
    b10 = [result[1] for result in b7]
    b11 = [result[2][0][2] for result in b7]
    b12 = [result[2][0][3] for result in b7]
    return list(zip(b8, b9, b10, b11, b12))
b13 = pd.DataFrame(fonk1(b7))
b14 = []
b15 = []
b16 = []
b17 = []
for b5 in range(0,b13.__len__()):
    b14.append(b13[1][b5][0])
for j in range(0,b13.__len__()):
    b15.append(b13[0][j])
b16.append(b14[0])
b16.append(b14[1])
b16.append(b14[2])
b16.append(b14[4])
b16.append(b14[5])
b16.append(b14[9])
b16.append(b14[10])
b16.append(b14[16])
b16.append(b14[17])
b16.append(b14[21])
b16.append(b14[24])
b16.append(b14[32])
b16.append(b14[33])
b16.append(b14[35])
b16.append(b14[42])
b16.append(b14[47])
b16.append(b14[50])
b16.append(b14[51])
b16.append(b14[55])
b17.append(b15[0])
b17.append(b15[1])
b17.append(b15[2])
b17.append(b15[4])
b17.append(b15[5])
b17.append(b15[9])
b17.append(b15[10])
b17.append(b15[16])
b17.append(b15[17])
b17.append(b15[21])
b17.append(b15[24])
b17.append(b15[32])
b17.append(b15[33])
b17.append(b15[35])
b17.append(b15[42])
b17.append(b15[47])
b17.append(b15[50])
b17.append(b15[51])
b17.append(b15[55])
   README Content:
This is an online store developed using Django that makes use of k-means clustering and Apriori algorithms to make recommendations to its user. It is a part of my Bachelor's graduation thesis.
The training data is present in the `FYP.csv` file. It consists of 9400 sample orders. The scripts for k-means clustering and apriori algorithm are present in `k-means.py` and `apriori.py` files resepectively.
The environment is as follows:
- Python 3.6.7
- Anaconda 4.6.14
- Django 1.11.3
To train the data, please see the files mentioned above and execute them. To run the website, execute the code `python manage.py runserver` within the directory in the command line. Then on your browser, visit `http:
