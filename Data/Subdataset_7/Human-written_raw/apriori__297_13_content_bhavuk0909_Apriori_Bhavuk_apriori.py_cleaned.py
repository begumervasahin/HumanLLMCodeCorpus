13. Repository: bhavuk0909/Apriori
   File: Bhavuk_apriori.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
b2 = []
for i in range(0, 7501):
    b2.append([str(b1.values[i,j]) for j in range(0, 20)])
from apyori import apriori
b3 = apriori(b2, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
b4 = list(b3)
   README Content:
The Apriori algorithm is a categorization algorithm. Some algorithms are used to create binary appraisals of information or find a regression relationship. Others are used to predict trends and patterns that are originally identified. Apriori is a basic machine learning algorithm which is used to sort information into categories. Sorting information can be incredibly helpful with any data management process. It ensures that data users are appraised of new information and can figure out the data that they are working with.
