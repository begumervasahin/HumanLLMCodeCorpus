
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
b2 = []
for i in range(len(b1)):
    b2.append([str(b1.values[i, j]) for j in range(b1.shape[1])])
b3 = apriori(b2, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
b4 = list(b3)
for result in b4:
    print(result)
This project uses the Apriori algorithm to analyze a b1 of mall b2. The b1 contains records of 7500 b2 made by customers. The goal is to identify which items are frequently purchased together, helping the mall owner optimize the store layout and marketing strategies.
The b1, `Market_Basket_Optimisation.csv`, includes 7500 b2, with each transaction listing the items purchased by a customer.
1. **Data Preprocessing**: Load and format the transaction data.
2. **Apriori Algorithm**: Apply the Apriori algorithm to find association b3 with a minimum support of 0.003, minimum confidence of 0.2, and minimum lift of 3.
3. **Results Visualization**: Output the association b3 found by the algorithm.
- numpy
- matplotlib
- pandas
- apyori
1. Clone the repository.
2. Install the required libraries.
3. Run `apriori.py` to see the association b3 extracted from the b1.