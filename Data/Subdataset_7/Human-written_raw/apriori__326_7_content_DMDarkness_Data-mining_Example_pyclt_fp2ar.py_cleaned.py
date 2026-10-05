7. Repository: DMDarkness/Data-mining
   File: Example_pyclt_fp2ar.py
   URL: https:
   Code Content:
import pyclt
import fp2ar
import re
def fonk1(dName):
    b1 = open(dName)
    b2 = []
    b3 = b1.readlines()
    for line in b3:
        b4 = re.split(' |\n',line)
        b5 = []
        for item in b4:
            if item.isdigit():
                b5.append(int(item))
        if(len(b5)>0):
            b2.append(b5)
    b1.close()
    return b2
b6 = fonk1("kosarak.dat")
[fi, sN]=pyclt.getFP(b6, 0.03, 0.005, 0.01)
b7 = fp2ar.getAR(fi,sN,0.75,1)
   README Content:
Some algorithms to form frequent itemsets/association rules from datasets, where many techniques, such as FP-tree, Apriori, PSO, GA, Granular computing, Central limit theorem and so on, are applied
Any `.pyd` can be put in the working directory and be imported by Python, which is also implemented by c++. The details of usage can be found in `How to use.py`.
1. FP-Growth: `pyfpgrowth.pyd` is the corresponding `.pyd`.
2. FPtorules: a function to form association rules from frequent patterns, `FPtorules.py` is the corresponding implementation.
3. BPSO-HD: A BPSO (Binary Particle Swarm Optimization) based algorithm mining long frequent patterns. `pybpsohd.pyd` is the corresponding `.pyd`. This is the corresponding [paper](https:
4. CLT: A Central Limit Theorem based algorithm mining frequent patterns. `pyclt.pyd` is the corresponding `.pyd`.
5. ARMGA: A GA (Genetic Algorithm) based algorithm mining association rules. `pyarmga.pyd` is the corresponding `.pyd`.
