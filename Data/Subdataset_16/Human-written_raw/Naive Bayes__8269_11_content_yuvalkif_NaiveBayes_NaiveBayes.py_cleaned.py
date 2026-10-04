import csv
import pandas as pd
import numpy as np
import DataPreProcessing as dp
class class1:
    def fonk1(self,b5):
        self.a1 = 2
        self.b1 = dict()
        self.b2 = dict()
        self.a2 = 0
        self.b3 = []
        self.b4 = []
        self.a3 = 0
        self.b5 = b5
        self.b6 = False
    '''
    @b7 : the b7 to be classified
    '''
    def fonk2(self , b7):
        self.a2 = b7.shape[0]
        self.b1 = self.fonk3(b7)
        b7 = dp.fillDatasetNANumerical(b7)
        b7 = dp.fillDatasetNACategorical(b7)
        b7 = dp.discretizeDataset(b7 , self.b5)
        self.fonk4(b7 = b7,classvalues=list(self.b1.keys()))
        self.b8 = True
    '''
        count unique values in the 'class' column
    '''
    def fonk3(self , b7):
        b9 = b7['class'].unique()
        self.b3 = b9
        b1 = dict()
        for b14 in b9:
            b1[b14] = 0
        for index, class2 in b7.iterrows():
            b1[class2['class']] += 1
        return b1
    '''
        given a column name and a class class2 , calculate joint frequency in the
        column for each unique column class2
    '''
    def fonk4(self , b7 , classvalues):
        b10 = []
        b11 = list(b7)
        b11 = b11[0:len(b11)-1]
        self.b4 = b11
        for colname in b11:
            b12 = list(b7[colname].unique())
            b10.append(float(1/len(b12)))
            b13 = dict()
            for classvalue in classvalues:
                for b14 in b12:
                    b14 = str(b14)
                    b13[b14+'_'+str(classvalue)] = 0
                    for index,class2 in b7.iterrows():
                        if((class2[colname] == b14) and (class2['class'] == classvalue)):
                            b13[b14+'_'+classvalue] += 1
            self.b2[colname] = b13
        self.a3 = b10
        return b12
    def fonk5(self,test_file,out_path):
        b15 = []
        b16 = self.fonk6(test_file)
        for index,row in b16.iterrows():
            b17 = self.fonk7(row)
            b18 = self.fonk8(b17)
            b15.append(str(index+1)+" "+b18)
        self.fonk9(out_path,b15)
        return b15
    def fonk6(self,test_file):
        b16 = pd.read_csv(test_file)
        b16 = dp.fillDatasetNANumerical(b16)
        b16 = dp.fillDatasetNACategorical(b16)
        b16 = dp.discretizeDataset(b16 , self.b5)
        return b16
    def fonk7(self,row):
        b19 = []
        for b14 in self.b3:
            b20 = []
            a4 = 0
            for att_value,att_name in zip(row,self.b4):
                try:
                    b21 = float((self.b2[att_name][str(att_value)+'_'+str(b14)] +float(self.a1)*float(self.a3[a4]))/(self.b1[b14]+self.a1))
                    a4 = a4+1
                    b20.append(b21)
                except KeyError:
                    b20.append(float(1/self.a2))
            b22 = float(self.b1[b14])/float(self.a2)
            for att_score in b20:
                b22 = b22*att_score
            b19.append(b22)
        return b19
    def fonk8(self,classes_scores):
        a5 = -1
        a6 = -1
        for i in range(0,len(classes_scores)):
            if a5 < classes_scores[i]:
                a5 = classes_scores[i]
                a6 = i
        return self.b3[a6]
    def fonk9(self,path,b15):
        with open ('output.txt','w') as f:
            f.writelines("%s\n" % row for row in b15)