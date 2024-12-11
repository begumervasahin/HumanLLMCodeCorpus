import pandas as pd
import math
import numpy as np
from web_scraping.scraping import main_path
def fonk1(keywords):
    b1 = keywords.split()
    b2 = pd.read_csv(f"{main_path()}/data/Job_search.csv")
    b3 = {}
    for term in b1:
        b4 = sum(1 for field in b2['Job_Name'] if term.lower() in field.lower())
        b3[term] = math.log(len(b2) / (1 + b4))
    for term in b1:
        b5 = []
        for field in b2['Job_Name']:
            b6 = sum(1 for word in field.split() if word.lower() == term.lower())
            b5.append(b6 / len(field.split()) * b3[term])
        b2[term] = np.array(b5)
    b2['TF-IDF'] = b2[b1].sum(b7 = 1)
    b2 = b2.sort_values(by='TF-IDF', ascending=False)
    b2 = b2[b2['TF-IDF'] != 0]
    b8 = b2.iloc[:, :4]
    return b8