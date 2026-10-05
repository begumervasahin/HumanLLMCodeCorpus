
import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx",sheet_name="Export Worksheet")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx",sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx",sheet_name="wordfrequencyfinal")
b4 = pd.DataFrame(columns=['MCAT_Name','Subcat_ID','MCAT_Name&HighFrequencyWords'])
b5 = pd.DataFrame(columns=['MCAT_ID','MCAT_Name','Alt_Name','Subcat_ID','Stopword','Attribute'])
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_ALTMCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b6 = b3.set_index('SUBCAT ID').T.to_dict('list')
a1 = 0
a2 = 0
while(a1<len(b2)):
    if(b2.iloc[a1]["SUBCAT_ID"] in b6.keys() and a1<len(b2)):
        b7 = b2.iloc[a1]["SUBCAT_ID"]
        b8 = a1
        b9 = ""
        while(b2.iloc[a1]["SUBCAT_ID"] == b7 and a1<=len(b2)-1):
            b9 += b2.iloc[a1]["GLCAT_MCAT_NAME"]+" "
            a1 = a1+1
            if(a1 = =len(b2)):
                break
        b10 = set(b9.split(' '))
        b11 = ""
        for x in b10:
            if x not in b11:
                b11+=x + " "
        b4.set_value(a2,'MCAT_Name',b2.iloc[b8]["GLCAT_MCAT_NAME"])
        b4.set_value(a2,'Subcat_ID',b2.iloc[b8]["SUBCAT_ID"])
        b12 = b11 +" "+ str(b6[b2.iloc[b8]["SUBCAT_ID"]][0])
        b4.set_value(a2,'MCAT_Name&HighFrequencyWords',b12)
        a2 = a2+1
    else:
        b4.set_value(a2,'MCAT_Name',b2.iloc[a1]["GLCAT_MCAT_NAME"])
        b4.set_value(a2,'Subcat_ID',b2.iloc[a1]["SUBCAT_ID"])
        b4.set_value(a2,'MCAT_Name&HighFrequencyWords',b2.iloc[a1]["GLCAT_MCAT_NAME"])
        a1 = a1+1
        a2 = a2+1
b13 = b4[['Subcat_ID','MCAT_Name&HighFrequencyWords']].set_index('Subcat_ID').T.to_dict('list')
a1 = 0
a2 = 0
while(a1<len(b1)):
    if(b1.iloc[a1]["FK_GLCAT_CAT_ID"] in b13.keys() and a1<len(b1)):
        b7 = b1.iloc[a1]["FK_GLCAT_CAT_ID"]
        b14 = ""
        b15 = b13[b7][0]
        b16 = b1.iloc[a1]["GLCAT_ALTMCAT_NAME"]
        for x in b16.split(" "):
            if(x not in b15.split(" ")):
                b14 = b14 + " "+x
        b5.set_value(a2,'MCAT_ID',b1.iloc[a1]["GLCAT_MCAT_ID"])
        b5.set_value(a2,'MCAT_Name',b1.iloc[a1]["GLCAT_MCAT_NAME"])
        b5.set_value(a2,'Alt_Name',b1.iloc[a1]["GLCAT_ALTMCAT_NAME"])
        b5.set_value(a2,'Subcat_ID',b7)
        b5.set_value(a2,'Stopword',b15)
        b5.set_value(a2,'Attribute',b14)
        a1 = a1+1
        a2 = a2+1
        if(a1 = =len(b1)):
                break
    else:
        b7 = b1.iloc[a1]["FK_GLCAT_CAT_ID"]
        b5.set_value(a2,'MCAT_ID',b1.iloc[a1]["GLCAT_MCAT_ID"])
        b5.set_value(a2,'MCAT_Name',b1.iloc[a1]["GLCAT_MCAT_NAME"])
        b5.set_value(a2,'Alt_Name',b1.iloc[a1]["GLCAT_ALTMCAT_NAME"])
        b5.set_value(a2,'Subcat_ID',b7)
        b14 = ""
        if(b7 in b6.keys()):
            b15 = b6[b7][0]
            b16 = b1.iloc[a1]["GLCAT_ALTMCAT_NAME"]
            for x in b16.split(" "):
                if(x not in b15.split(" ")):
                    b14 = b14 + " "+x
            b5.set_value(a2,'Stopword',b15)
            b5.set_value(a2,'Attribute',b14)
        a1 = a1+1
        a2 = a2+1
        if(a1 = =len(b1)):
            break
b5['Attribute']=b5['Attribute'].str.lstrip()
b5.to_csv("stopwordsremovedaltnames.csv",b17 = False)