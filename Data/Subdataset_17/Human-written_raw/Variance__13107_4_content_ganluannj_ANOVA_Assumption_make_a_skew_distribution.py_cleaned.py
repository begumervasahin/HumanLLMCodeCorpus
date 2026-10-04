import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats
rangeofx=[-1.73,1.73]
def lessthan (listlessthan, alpha):
    lessthanlen=len (listlessthan)
    lessthan_i=0
    numberless=0.000
    while lessthan_i < lessthanlen:
        if listlessthan[lessthan_i]<alpha:
            numberless=numberless+1
        lessthan_i=lessthan_i+1
    percentage=numberless/lessthanlen
    return (percentage)
def pdf (x, uniformvalue):
    return (1-uniformvalue)*stats.norm.pdf(x)+0.289*uniformvalue
def findminandmax(rangen, uniformvalue1):
    minx=100000
    maxx=0
    listofrange=np.arange(rangen[0], rangen[1],0.01)
    listpoint=0
    returnlist=[]
    while listpoint<len(listofrange):
        number=listofrange[listpoint]
        if pdf(number, uniformvalue1)< minx:
            minx=pdf(number, uniformvalue1)
        if pdf(number, uniformvalue1)>maxx:
            maxx=pdf(number, uniformvalue1)
        listpoint=listpoint+1
    returnlist.append(minx)
    returnlist.append(maxx)
    return returnlist
p=0
while p<0.01:
    minofy=findminandmax(rangeofx,p)[0]
    maxofy=findminandmax(rangeofx,p)[1]
    times=0
    pvaluelist=[]
    while times<1000:
        i=0
        list1=[]
        while i<100:
            x=np.random.uniform(rangeofx[0],rangeofx[1])
            y=np.random.uniform (minofy, maxofy)
            if y<pdf (x,p):
                list1.append(x)
                i=i+1
            else:
                i=i
        pvaluei=stats.normaltest(list1)[1]
        pvaluelist.append(pvaluei)
        times=times+1
    print p
    print lessthan(pvaluelist,0.05)
    p=p+0.1