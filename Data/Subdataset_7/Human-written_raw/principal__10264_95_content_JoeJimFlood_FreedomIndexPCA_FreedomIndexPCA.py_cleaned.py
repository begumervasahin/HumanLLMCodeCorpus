'''
All b4 are index values for 2014
Sources
-------
Fraser Institute's Economic Freedom of the World Index: https:
Cato Institute's Personal Freedom Index: https:
Social Progress Imperative's Social Progress Index: https:
*original b4 were divided by 10 so that all three indices had values between 0 and 10
'''
import numpy as np
import pandas as pd
import os
from scipy.stats import norm
from scipy.special import erfinv
b1 = os.path.split(__file__)[0]
b2 = os.path.join(b1, 'IndexData.csv')
b3 = os.path.join(b1, 'IndexCorrelations.csv')
b4 = pd.read_csv(b2).dropna()
b5 = (b4[['Economic', 'Personal', 'Social']].copy())
b5 -= b5.mean(0)
b6 = b5.shape[0]
(U, S, VT) = np.linalg.svd(b5.T/np.sqrt(b6-1))
b7 = np.dot(U.T, b5.T).T
b4['Combined'] = -b7[:, 0]
b4['Combined'] += (5 - b4['Combined'].mean())
b4.set_index('Countries (2014)').sort_values('Combined', b8 = False).to_csv(b2)
b4.corr().to_csv(b3)