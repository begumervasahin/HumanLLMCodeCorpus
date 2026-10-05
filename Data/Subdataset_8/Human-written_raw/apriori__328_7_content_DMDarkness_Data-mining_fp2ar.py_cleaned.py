7. Repository: DMDarkness/Data-mining
   File: fp2ar.py
   URL: https:
   Code Content:
def getSubSet(pat,sub1,sub2,L,temp,base):
    if(L<1):
        if(sub1.count(temp)==0):
            temp.sort()
            pat.sort()
            sub1.append(temp)
            sub2.append(pat)
    else:
        for i in range(base,len(pat)):
            getSubSet(pat[0:i]+pat[i+1:],sub1,sub2,L-1,temp+[pat[i]], i)
def getAR(fi,N,minconf,minlift):
    Rule=[]
    fiNum=len(fi)
    fid={}
    for i in range(0,fiNum):
        fii=fi[i][0:-1]
        fii.sort()
        fid[tuple(fii)]=fi[i][-1]
    for i in range(0,fiNum):
        psLen=int((len(fi[i])-1)/2)
        pat=fi[i][0:-1]
        sup1=fi[i][-1]
        sub1=[]
        sub2=[]
        for j in range(1,psLen+1):
            getSubSet(pat,sub1,sub2,j,[],0)
        for j in range(0,len(sub1)):
            if(sub1.count(sub2[j])!=0):
                sub1[j]=[-1,-9]
                sub2[j]=[-2,-5]
            pat2=sub1[j]
            pat3=sub2[j]
            pat2.sort()
            pat3.sort()
            if(fid.has_key(tuple(pat2)) and fid.has_key(tuple(pat3))):
                sup2=fid[tuple(pat2)]
                sup3=fid[tuple(pat3)]
                if(sup1*N*1.0/(sup2*sup3*1.0) > minlift):
                    if(sup1*1.0/sup2 > minconf):
                        newrule=[pat2,pat3,sup1,sup1*1.0/sup2,sup1*N*1.0/(sup2*sup3*1.0)]
                        Rule.append(newrule)
                    if(sup1*1.0/sup3 > minconf):
                        newrule=[pat3,pat2,sup1,sup1*1.0/sup3,sup1*N*1.0/(sup2*sup3*1.0)]
                        Rule.append(newrule)
    return Rule
   README Content:
Some algorithms to form frequent itemsets/association rules from datasets, where many techniques, such as FP-tree, Apriori, PSO, GA, Granular computing, Central limit theorem and so on, are applied
Any `.pyd` can be put in the working directory and be imported by Python, which is also implemented by c++. The details of usage can be found in `How to use.py`.
1. FP-Growth: `pyfpgrowth.pyd` is the corresponding `.pyd`.
2. FPtorules: a function to form association rules from frequent patterns, `FPtorules.py` is the corresponding implementation.
3. BPSO-HD: A BPSO (Binary Particle Swarm Optimization) based algorithm mining long frequent patterns. `pybpsohd.pyd` is the corresponding `.pyd`. This is the corresponding [paper](https:
4. CLT: A Central Limit Theorem based algorithm mining frequent patterns. `pyclt.pyd` is the corresponding `.pyd`.
5. ARMGA: A GA (Genetic Algorithm) based algorithm mining association rules. `pyarmga.pyd` is the corresponding `.pyd`.
