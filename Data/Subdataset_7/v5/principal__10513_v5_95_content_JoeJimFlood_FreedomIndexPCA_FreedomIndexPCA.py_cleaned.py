import numpy as np
import pandas as pd
import os
from scipy.stats import norm
from scipy.special import erfinv
b1 = os.path.dirname(__file__)
b2 = os.path.join(b1, 'IndexData.csv')
b3 = os.path.join(b1, 'IndexCorrelations.csv')
b4 = pd.read_csv(b2).dropna()
b5 = ['Economic', 'Personal', 'Social']
b6 = b4[b5].copy()
b7 = b6 - b6.mean()
U, S, b8 = np.linalg.svd(b7.T / np.sqrt(b7.shape[0] - 1))
b9 = np.dot(U.T, b7.T).T
b10 = -b9[:, 0]
b10 += (5 - b10.mean())
b4['Combined'] = b10
b11 = b4.set_index('Countries (2014)').sort_values('Combined', ascending=False)
b11.to_csv(b2)
b12 = b4.corr()
b12.to_csv(b3)