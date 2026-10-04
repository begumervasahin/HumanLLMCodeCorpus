
import os
import pandas as pd
def getFilelist(a):
    path = a
    filelist = []
    files = os.listdir(path)
    for f in files:
        filelist.append(f)
    return filelist
allfile = getFilelist('/TF-IDF')
allfile1 = getFilelist('/TF-IDF1')
os.chdir('/TF-IDF')
path = '/TF-IDF1'
j = 0
for i in allfile:
    if i not in allfile1:
        try:
            a=pd.read_csv(i,sep='    ',header=None,engine='python')
            a1=a[a[1]>0]
            a1=a1.sort_values(by = [1],axis = 0,ascending = False)
            if len(a1) <=50:
                filename=i.replace('.txt','')
                path1 = path+'/'+filename+'.txt'
                a1.to_csv(path1,sep='\t',header=None,index=False)
            else:
                a2 = a1.iloc[0:50,:]
                filename=i.replace('.txt','')
                path1 = path+'/'+filename+'.txt'
                a2.to_csv(path1,sep='\t',header=None,index=False)
        except Exception as e:
            j = j+1
print('æ§è¡å®æ¯ï¼')