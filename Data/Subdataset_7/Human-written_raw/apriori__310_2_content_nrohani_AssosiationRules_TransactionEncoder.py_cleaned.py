2. Repository: nrohani/AssosiationRules
   File: class1.py
   URL: https:
   Code Content:
import numpy as np
from scipy.b5 import csr_matrix
from sklearn.base import BaseEstimator, TransformerMixin
class class1(BaseEstimator, TransformerMixin):
    def fonk1(self):
        return None
    def fonk2(self, X):
        b1 = set()
        for transaction in X:
            for item in transaction:
                b1.add(item)
        self.b2 = sorted(b1)
        b3 = {}
        for b8, item in enumerate(self.b2):
            b3[item] = b8
        self.b4 = b3
        return self
    def fonk3(self, X, b5 = False):
        if b5:
            b6 = [0]
            b7 = []
            for transaction in X:
                for item in set(transaction):
                    b8 = self.b4[item]
                    b7.append(b8)
                b6.append(len(b7))
            b9 = [True]*len(b7)
            b10 = csr_matrix((b9, b7, b6),
                               b11 = bool)
        else:
            b10 = np.zeros((len(X), len(self.b2)), b11=bool)
            for row_idx, transaction in enumerate(X):
                for item in transaction:
                    b8 = self.b4[item]
                    b10[row_idx, b8] = True
        return b10
    def fonk4(self, b10):
        return [[self.b2[idx]
                 for idx, cell in enumerate(row) if cell]
                for row in b10]
    def fonk5(self, X, b5 = False):
        return self.fonk2(X).fonk3(X, b5 = b5)
   README Content:
Implementation of Eclat and Apriori algorithms to find association rules in the store with Python language
![Image description](https:
----------------------------------------------------------------------------------------------------------
Min_sup	Min_conf Rule number
0.02	0.6	0
0.02	0.5	1
0.001	0.06	13050
0.0009	0.00095	13335
0.000825	0.09	15047
0.0009	0.0001	16030
0.00085	0.0035	16030
0.0008	0.05	19590
0.00078	0.001	19818
--------------------------------------------------------------------------------------------------------
No	Rules	 Support 	 Confidence 	 Lift
1	['dishes', 'bottled beer'] -> ['liquor (appetizer)']	0.00061	0.428571	54.03846
2	['herbs', 'citrus fruit'] -> ['turkey']	0.000712	0.241379	29.67457
3	['fruit/vegetable juice', 'root vegetables', 'other vegetables', 'tropical fruit'] -> ['turkey']	0.00061	0.24	29.505
4	['ham', 'other vegetables', 'sliced cheese'] -> ['soft cheese']	0.00061	0.5	29.27083
5	['root vegetables', 'cream cheese ', 'domestic eggs'] -> ['soft cheese']	0.000712	0.4375	25.61198
6	['fruit/vegetable juice', 'root vegetables', 'tropical fruit'] -> ['turkey']	0.00061	0.1875	23.05078
7	['margarine', 'other vegetables', 'chocolate marshmallow'] -> ['waffles']	0.00061	0.857143	22.30159
8	['liquor', 'bottled beer'] -> ['red/blush wine']	0.001932	0.413043	21.49356
9	['root vegetables', 'canned fish'] -> ['salt']	0.00061	0.230769	21.41147
10	['root vegetables', 'domestic eggs', 'pip fruit'] -> ['salt']	0.00061	0.230769	21.41147
11	['root vegetables', 'sausage', 'other vegetables', 'citrus fruit'] -> ['soft cheese']	0.00061	0.352941	20.66176
12	['frankfurter', 'ham', 'processed cheese'] -> ['white bread']	0.00061	0.857143	20.36232
13	['butter', 'Instant food products'] -> ['hamburger meat']	0.000813	0.666667	20.05097
14	['baking powder', 'flour', 'margarine'] -> ['sugar']	0.00061	0.666667	19.68969
15	['flour', 'margarine', 'curd'] -> ['sugar']	0.00061	0.666667	19.68969
16	['bottled water', 'other vegetables', 'fruit/vegetable juice'] -> ['rice']	0.00061	0.15	19.67
17	['long life bakery product', 'coffee'] -> ['mayonnaise']	0.00061	0.176471	19.28431
18	['beef', 'coffee'] -> ['frozen potato products']	0.00061	0.162162	19.21524
19	['fruit/vegetable juice', 'hard cheese'] -> ['rice']	0.00061	0.146341	19.19024
20	['mustard', 'chocolate'] -> ['oil']	0.000813	0.533333	19.00483
21	['popcorn', 'bottled beer'] -> ['salty snack']	0.000712	0.7	18.50672
22	['domestic eggs', 'other vegetables', 'hard cheese'] -> ['soft cheese']	0.00061	0.315789	18.48684
23	['ham', 'tropical fruit', 'processed cheese'] -> ['white bread']	0.000712	0.777778	18.47692
24	['bottled water', 'beef'] -> ['jam']	0.00061	0.098361	18.2524
25	['Instant food products', 'domestic eggs'] -> ['hamburger meat']	0.00061	0.6	18.04587
26	['ham', 'sliced cheese'] -> ['soft cheese']	0.000813	0.307692	18.01282
27	['domestic eggs', 'rolls/buns', 'processed cheese'] -> ['white bread']	0.00061	0.75	17.81703
28	['shopping bags', 'ham', 'processed cheese'] -> ['white bread']	0.00061	0.75	17.81703
29	['flour', 'margarine', 'citrus fruit'] -> ['sugar']	0.00061	0.6	17.72072
30	['tropical fruit', 'semi-finished bread'] -> ['turkey']	0.00061	0.142857	17.562
------------------------------------------------------------------------------------------
