7. Repository: DMDarkness/Data-mining
   File: Example_pyarmga.py
   URL: https:
   Code Content:
import pyarmga as ga
import re
def read(dName):
    f = open(dName)
    Trans=[]
    content  = f.readlines()
    for line in content:
        sline=re.split(' |\n',line)
        trans=[]
        for item in sline:
            if item.isdigit():
                trans.append(int(item))
        if(len(trans)>0):
            Trans.append(trans)
    f.close()
    return Trans
dataset=read("kosarak.dat")
ar=ga.getAR(dataset, 0.7, 1, 30, 30, 0.25, 1, 1, 10)
   README Content:
Some algorithms to form frequent itemsets/association rules from datasets, where many techniques, such as FP-tree, Apriori, PSO, GA, Granular computing, Central limit theorem and so on, are applied
Any `.pyd` can be put in the working directory and be imported by Python, which is also implemented by c++. The details of usage can be found in `How to use.py`.
1. FP-Growth: `pyfpgrowth.pyd` is the corresponding `.pyd`.
2. FPtorules: a function to form association rules from frequent patterns, `FPtorules.py` is the corresponding implementation.
3. BPSO-HD: A BPSO (Binary Particle Swarm Optimization) based algorithm mining long frequent patterns. `pybpsohd.pyd` is the corresponding `.pyd`. This is the corresponding [paper](https:
4. CLT: A Central Limit Theorem based algorithm mining frequent patterns. `pyclt.pyd` is the corresponding `.pyd`.
5. ARMGA: A GA (Genetic Algorithm) based algorithm mining association rules. `pyarmga.pyd` is the corresponding `.pyd`.
