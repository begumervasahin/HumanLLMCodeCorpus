11. Repository: rjtmahinay/fuzzy-association-rule-mining
   File: Apriori.py
   URL: https:
   Code Content:
from itertools import chain, combinations
def fonk1(filename):
    b1 = open(filename, 'rU')
    for b2 in b1:
        b2 = b2.strip().rstrip(',')
        b3 = frozenset(b2.split(','))
        yield b3
def fonk2(b24):
    b4 = set()
    b5 = list()
    for b3 in b24:
        b5.append(frozenset(b3))
        for item in b3:
            if item:
                b4.add(frozenset([item]))
    return b4, b5
def fonk3(b5, b4, b6 = 0):
    b7 = len(b5)
    b2 = [
        (item, float(sum(1 for b3 in b5 if item.issubset(b3))) / b7)
        for item in b4
    ]
    return dict([(item, support) for item, support in b2 if support >= b6])
def fonk4(b5, b9, b6):
    b8 = dict()
    a1 = 1
    while True:
        if a1 > 1:
            b9 = fonk5(b10, a1)
        b10 = fonk3(b5, b9, b6)
        if not b10:
            break
        b8.update(b10)
        a1 += 1
    return b8
def fonk5(b4, a1):
    return set([i.union(j) for i in b4 for j in b4 if len(i.union(j)) == a1])
def fonk6(b4):
    return chain(*[combinations(b4, i + 1) for i, a in enumerate(b4)])
def fonk7(b8, min_confidence, min_lift):
    b11 = list()
    for item, support in b8.items():
        if len(item) > 1:
            for b13 in fonk6(item):
                b12 = item.difference(b13)
                if b12:
                    b13 = frozenset(b13)
                    b14 = b13.union(b12)
                    b15 = float(b8[b14]) / b8[b13]
                    b16 = b15 / (b8[b13] * b8[b12])
                    if b15 >= min_confidence:
                        if b16 >= min_lift:
                            b11.append((b13, b12, b15, b16))
    return b11
def fonk8(b24, b6, min_confidence, min_lift):
    b17 = fonk1(b24)
    b4, b5 = fonk2(b17)
    b8 = fonk4(b5, b4, b6)
    b11 = fonk7(b8, min_confidence, min_lift)
    return b11
def fonk9(b11):
    print('--Rules--')
    for b13, b12, b15, b16 in sorted(b11, b18 = lambda iterator: iterator[0]):
        print('RULES: {} => {} : {} : {}'.format(tuple(b13), tuple(b12), round(b15, 5),
                                                 round(b16, 3)))
def fonk10(b11, frequent_itemset):
    b19 = []
    b20 = []
    b21 = []
    b22 = []
    b16 = []
    for b13, b12, b15, b16 in sorted(b11, b18 = lambda iterator: iterator[0]):
        b20.append(tuple(b13))
        b21.append(tuple(b12))
        b22.append(round(b15, 4))
        b16.append(round(b16, 3))
    return b20, b21, b22, b16
def fonk11(b17, b23 = 0.014, default_confidence=0.9, default_lift=1):
    b24 = fonk1(b17)
    b11, b4 = fonk8(b24, b23, default_confidence, default_lift)
    return fonk10(b11, b4)
   README Content:
*This is an accepted paper at the 3rd IEEE International Conference on Agents (ICA 2018)*
This paper applies FP-Growth algorithm in mining fuzzy association b11 for a prediction system of dengue. The system mines its b11 through input of historic predictor variables for dengue. The b11 will be used to build a rule-based classifier to predict the dengue incidence for the next month for the years 2001-2006 in the Philippines. The FP-Growth Algorithm was compared to Apriori Algorithm by Sensitivity, Specificity, PPV, NPV, execution time and memory usage. The results showed that FP-Growth Algorithm is significantly better in execution time, numerically better in memory and comparable in Sensitivity, Specificity PPV and NPV to Apriori Algorithm.
The following default values were used in this research based on the b24:
Support: 0.014 <br />
Confidence: 0.9
Generate association b11
```
b11 = Apriori.fonk8(b24, support, b15, b16)
```
Print association b11
```
Apriori.fonk9(b11)
```
Generate association b11
```
b11 = FPGrowth.generate_patterns_rules(b24, support, b15)
```
Print association b11
```
FPGrowth.fonk9(b11)
```
*  [**Reynaldo John Tristan Mahinay Jr.**](https:
* **Franz Stewart Dizon**
* [**Stephen Kyle Farinas**](https:
* **Harry Pardo**
The results are showed in this link - [Comparison Result](https:
    Copyright (c) 2018 Reynaldo John Tristan Mahinay Jr., Franz Stewart Dizon, Stephen Kyle Farinas and Harry Pardo
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
