4. Repository: JunaidAShaikh/Apriori_and_Association_Rule_Generation_Algorithm
   File: Project1_Apriori_PartA.py
   URL: https:
   Code Content:
import numpy as np
import time
from datetime import datetime
a1 = 0
b1 = []
b2 = {}
a2 = 70
a3 = 50
b3 = 'associationruletestdata.txt'
def fonk1(rule,body):
    global a1
    global a2
    a4 = 0.0
    a5 = 0.0
    b4 = list(sorted(set(rule)-set(body)))
    for record in range (a1):
        b5 = True
        for element in body:
            b6 = int(element[0:3])
            b7 = element[4:]
            if b7 = = "Up":
                if (b1[record][b6-1]) == 0:
                    b5 = False
                    break
            elif b7 = = "Down":
                if (b1[record][b6-1]) == 1:
                    b5 = False
                    break
            elif  (b1[record][b6-1]) != b2[b7]:
                b5 = False
                break
        if(b5 = =True):
            a5 += 1.0
        else:
            continue
        b5 = True
        for element in b4:
            b6 = int(element[0:3])
            b7 = element[4:]
            if b7 = = "Up":
                if (b1[record][b6-1]) == 0:
                    b5 = False
                    break
            elif b7 = = "Down":
                if (b1[record][b6-1]) == 1:
                    b5 = False
                    break
            elif  (b1[record][b6-1]) != b2[b7]:
                b5 = False
                break
        if(b5 = =True):
            a4 += 1.0
    if((a4/a5)*100 >= a2) :
        return True
    else:
        return False
def fonk2(b25,a8,b19):
    for prev in b19:
        b8 = list(set(b25).intersection(prev))
        if len(b8)==(a8-1):
            print("Infrequent from previois Interation")
            return False
    return True
def fonk3():
    global a1
    global b1
    global b2
    global a3
    global b3
    b1 = []
    a6 = 0
    a1 = 0
    b9 = []
    with open(b3,'r') as f:
        for line in f:
            a1 = a1 +1
            b10 = []
            b10 = line.split('\t')
            b11 = b10[-1].strip()
            b9.append(b11)
            b10 = b10[:-1]
            a6 = len(b10)
            for index, b12 in enumerate(b10):
                if b12 = = "Down":
                    b10[index]=0
                elif b12 = = "Up":
                    b10[index]=1
                else:
                    print("Bhakk Saala")
            b1.append(b10)
    b1 = np.array(b1)
    b13 = sorted(set(b9))
    b14 = list(b13)
    b2 = {}
    for name in b14:
        b2[name] = b14.index(name)
    b15 = np.zeros((a1,1))
    b1 = np.hstack((b1,b15))
    a7 = 0
    for x in b9:
        b1[a7][a6]= b2[x]
        a7 = a7 + 1
    a8 = 1
    b16 = []
    b17 = []
    b18 = []
    b19 = []
    b20 = []
    for i in range(a6):
        b17 = []
        b21 = '{b21:03d}'.format(b21=(i+1))
        b21 = str(b21)
        b17.append(b21+"_Down")
        b16.append(b17)
        b17 = []
        b17.append(str(b21+"_Up"))
        b16.append(b17)
    b16 = sorted(b16)
    a6 = a6 + 1
    for x in b14:
        b17 = []
        b21 = '{b21:03d}'.format(b21=(a6))
        b21 = str(b21)
        b17.append(b21+"_"+str(x))
        b16.append(b17)
    b22 = []
    while (a8 <= a6):
        b18 = []
        b20 = []
        for current_list in b16:
            a9 = 0
            for record in range (a1):
                b5 = True
                for element in current_list:
                    b6 = int(element[0:3])
                    b7 = element[4:]
                    if b7 = = "Up":
                        if (b1[record][b6-1]) == 0:
                            b5 = False
                            break
                    elif b7 = = "Down":
                        if (b1[record][b6-1]) == 1:
                            b5 = False
                            break
                    elif  (b1[record][b6-1]) != b2[b7]:
                        b5 = False
                        break
                if(b5 = =True):
                    a9 = a9+1
                    if(a9  >= a3):
                        break
            if(a9 < a3):
                b20.append(current_list)
            else:
                b18.append(current_list)
        if(len(b18)==0):
            print("No Supported Cominations of a8 equal and greater than " + str(a8))
            break
        print("Supported Combinations of size "+str(a8) + "  "+ str(len(b18)))
        b22.append(b18)
        b16 = []
        a8 = a8 + 1
        b23 = False
        if a8!=2:
            for element1_idx, element1 in enumerate(b18):
                    for element2_idx in range(element1_idx+1, len(b18)):
                        b24 = b18[element2_idx]
                        for i in range(a8-2):
                            if element1[i]!=b24[i]:
                                b23 = True
                                break
                        if b23:
                            b23 = False
                            continue
                        b25 = []
                        b25 = list(sorted(set(element1+b24)))
                        if fonk2(b25,a8,b19):
                            b16.append(b25)
        else:
            for element1_idx, element1 in enumerate(b18):
                for element2_idx in range(element1_idx+1, len(b18)):
                    b24 = b18[element2_idx]
                    b16.append(element1+b24)
        b16 = set(tuple(x) for x in b16)
        b16 = list(tuple(x) for x in b16)
        if(len(b16)==0):
            print("No Cominations of a8 and after" + str(a8))
            break
        b19 = b20
    return b22
def fonk4():
    b26 = datetime.now()
    b22 = fonk3()
    return b22
if b27 = ="__main__":
    fonk4()
   README Content:
CSE601: Data Mining and Bioinformatics :  Implementation of Apriori algorithm and Association rule generation algorithm for Frequent Itemsets and Association rule mining of gene expression data.
Associative Analysis b28 = ====================================
- Execute the main.py file using the command "python main.py"
- You will be asked whether you want to input the Queries through file or console. If through file, type "file" and press enter (Code will read queries from 'rules.txt' file) and,
If through console, type "console" and press enter. Now enter you Query and press enter to see the result
- Modify b3 variable in main function of file main.py to change the file from where to read Queries (if you selected "file" above,currently its "rules.txt")
- set debugging_on variable in main function of file main.py to False if you want only rule a9, else to True if you want rule counts and also print all the rules
-Modify b3 global variable in Project1_Apriori_PartA.py to specify the input file from where to read input data(currently its set to 'associationruletestdata.txt').
-Modify a2 and a3 which are global variables in Project1_Apriori_PartA.py to modify Confidence and minsupport respectively
