import pandas as pd
import math
import numpy as np
from web_scraping.scraping import *
def fonk1(keywords):
    b1 = keywords
    b2 = b1.split()
    b3 = dict()
    b4 = pd.read_csv("%s/data/Job_search.csv" % main_path(), index_col=None)
    b5 = b4['Job_Name'].tolist()
    for key in b2:
        a1 = 0
        for field in b5:
            if key in field:
                a1 += 1
        b3[key] = math.log(len(b4.index)/1+a1)
    b4['TF-IDF'] = 0
    for key in b2:
        b6 = []
        for field in b5:
            a2 = 0
            b7 = field.split()
            for i in b7:
                if key.lower() == i.lower():
                    a2 += 1
            b6.append(a2/len(b7))
        b4[key] = np.array(b6)
        b4[key] = b4[key]*b3[key]
        b4['TF-IDF'] = b4['TF-IDF'] + b4[key]
    b4 = b4.sort_values(by=['TF-IDF'], ascending=False)
    b4 = b4.loc[b4['TF-IDF'] != 0]
    b4 = b4.iloc[:, :4]
    return b4