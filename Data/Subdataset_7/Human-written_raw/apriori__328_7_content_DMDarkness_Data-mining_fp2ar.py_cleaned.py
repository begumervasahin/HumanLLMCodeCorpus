7. Repository: DMDarkness/Data-mining
   File: fp2ar.py
   URL: https:
   Code Content:
def fonk1(b6,b8,b9,L,temp,base):
    if(L<1):
        if(b8.count(temp)==0):
            temp.sort()
            b6.sort()
            b8.append(temp)
            b9.append(b6)
    else:
        for i in range(base,len(b6)):
            fonk1(b6[0:i]+b6[i+1:],b8,b9,L-1,temp+[b6[i]], i)
def fonk2(fi,N,minconf,minlift):
    b1 = []
    b2 = len(fi)
    b3 = {}
    for i in range(0,b2):
        b4 = fi[i][0:-1]
        b4.sort()
        b3[tuple(b4)]=fi[i][-1]
    for i in range(0,b2):
        b5 = int((len(fi[i])-1)/2)
        b6 = fi[i][0:-1]
        b7 = fi[i][-1]
        b8 = []
        b9 = []
        for j in range(1,b5+1):
            fonk1(b6,b8,b9,j,[],0)
        for j in range(0,len(b8)):
            if(b8.count(b9[j])!=0):
                b8[j]=[-1,-9]
                b9[j]=[-2,-5]
            b10 = b8[j]
            b11 = b9[j]
            b10.sort()
            b11.sort()
            if(b3.has_key(tuple(b10)) and b3.has_key(tuple(b11))):
                b12 = b3[tuple(b10)]
                b13 = b3[tuple(b11)]
                if(b7*N*1.0/(b12*b13*1.0) > minlift):
                    if(b7*1.0/b12 > minconf):
                        b14 = [b10,b11,b7,b7*1.0/b12,b7*N*1.0/(b12*b13*1.0)]
                        b1.append(b14)
                    if(b7*1.0/b13 > minconf):
                        b14 = [b11,b10,b7,b7*1.0/b13,b7*N*1.0/(b12*b13*1.0)]
                        b1.append(b14)
    return b1
   README Content:
Some algorithms to form frequent itemsets/association rules from datasets, where many techniques, such as FP-tree, Apriori, PSO, GA, Granular computing, Central limit theorem and so on, are applied
Any `.pyd` can be put in the working directory and be imported by Python, which is also implemented by c++. The details of usage can be found in `How to use.py`.
1. FP-Growth: `pyfpgrowth.pyd` is the corresponding `.pyd`.
2. FPtorules: a function to form association rules from frequent patterns, `FPtorules.py` is the corresponding implementation.
3. BPSO-HD: A BPSO (Binary Particle Swarm Optimization) based algorithm mining long frequent patterns. `pybpsohd.pyd` is the corresponding `.pyd`. This is the corresponding [paper](https:
4. CLT: A Central Limit Theorem based algorithm mining frequent patterns. `pyclt.pyd` is the corresponding `.pyd`.
5. ARMGA: A GA (Genetic Algorithm) based algorithm mining association rules. `pyarmga.pyd` is the corresponding `.pyd`.
