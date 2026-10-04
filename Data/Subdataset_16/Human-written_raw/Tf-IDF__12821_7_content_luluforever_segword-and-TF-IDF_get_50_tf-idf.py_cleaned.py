
import os
import pandas as pd
def fonk1(b6):
    b1 = b6
    b2 = []
    b3 = os.listdir(b1)
    for f in b3:
        b2.append(f)
    return b2
b4 = fonk1('/TF-IDF')
b5 = fonk1('/TF-IDF1')
os.chdir('/TF-IDF')
b1 = '/TF-IDF1'
b7 = 0
for i in b4:
    if i not in b5:
        try:
            b6 = pd.read_csv(i,b10='    ',header=None,engine='python')
            b7 = b6[b6[1]>0]
            b7 = b7.sort_values(by = [1],axis = 0,ascending = False)
            if len(b7) <=50:
                b8 = i.replace('.txt','')
                b9 = b1+'/'+b8+'.txt'
                b7.to_csv(b9,b10 = '\t',header=None,index=False)
            else:
                b11 = b7.iloc[0:50,:]
                b8 = i.replace('.txt','')
                b9 = b1+'/'+b8+'.txt'
                b11.to_csv(b9,b10 = '\t',header=None,index=False)
        except Exception as e:
            b7 = b7+1
print('æ§è¡å®æ¯ï¼')