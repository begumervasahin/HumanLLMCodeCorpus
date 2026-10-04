19. Repository: Haridut/Data-Mining-algorithms
   File: Frag_shell.py
   URL: https:
   Code Content:
import sys
import math
import itertools
dim1_list=[]
for i in range(0, len(item_list[0])):
    list1=[]
    for j in range(0,len(item_list)):
        list1.append(item_list[j][i])
    dim1_list.append(list1)
dim_list=[]
for i in dim1_list:
    dim_list.append(sorted(list(set(i))))
lista=[]
for i in range(0,partitions):
    lista.append([])
for j in range(0,len(item_list[0])):
    lista[j%partitions].append(j)
ind_count=[]
for i in lista:
    ind_count.append(len(i))
m=0
list_fragmented=[]
for i in range(0,partitions):
    listc=[]
    for j in range(0,ind_count[i]):
        listc.append(dim_list[m])
        m=m+1
    list_fragmented.append(listc)
def listcount (listd):
    l=0
    for p in item_list:
        if set(listd)<set(p):
            l=l+1
    return l
for i in range(len(list_fragmented)):
    cf=[]
    for j in range(len(list_fragmented[i])):
        for don in (list(itertools.combinations(range(len(list_fragmented[i])),j+1))):
            cf.append(list(don))
    for k in cf:
        list_comb=[]
        merger=[]
        for value in k:
            merger=merger+list_fragmented[i][value]
        for h in (list(itertools.combinations(merger,len(k)))):
            list_comb.append(list(h))
        for p in list_comb:
            count=listcount(p)
            if count is not 0:
                for d in range(len(p)):
                    print (str(p[d])+' ',end='')
                print(': '+ str(count))
    print()
   README Content:
This repository contains codes for Apriori algorithm, online query computation using shell-fragments.
