
import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx",sheet_name="Export Worksheet")
b2 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
b3 = pd.DataFrame(columns=['Subcat_ID','Stopwords'])
b4 = list(b1['SUBCAT_ID'].unique())
b2["HIGH FREQUENCY WORDS"] = b2["HIGH FREQUENCY WORDS"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b5 = b2.set_index('SUBCAT ID').T.to_dict('list')
a1 = 0
a2 = 0
a3 = 0
while(a1<len(b2)):
    if(b2.iloc[a1]["SUBCAT ID"] in b4 and a1<len(b2)):
        b6 = b2.iloc[a1]["SUBCAT ID"]
        b7 = a2
        b8 = ""
        while(b1.iloc[a2]["SUBCAT_ID"] == b6 and a2<=len(b1)-1):
            b8 += b1.iloc[a2]["GLCAT_MCAT_NAME"]+" "
            a2 = a2+1
            if(a2 = =len(b1)):
                break
        b9 = set(b8.split(' '))
        b10 = ""
        for x in b9:
            if x not in b10:
                b10+=x + " "
        b3.set_value(a3,'Subcat_ID',b1.iloc[b7]["SUBCAT_ID"])
        b11 = b10 +" "+ str(b5[b1.iloc[b7]["SUBCAT_ID"]][0])
        b3.set_value(a3,'Stopwords',b11)
        a3 = a3+1
        a1 = a1+1
    elif(b2.iloc[a1]["SUBCAT ID"] not in b4 and a1<len(b2)):
        b3.set_value(a3,'Subcat_ID',b2.iloc[a1]["SUBCAT ID"])
        b3.set_value(a3,'Stopwords',b2.iloc[a1]["HIGH FREQUENCY WORDS"])
        a3 = a3+1
        a1 = a1+1
b3.to_csv("700subcatwisefinalstopwords.csv",b12 = False)