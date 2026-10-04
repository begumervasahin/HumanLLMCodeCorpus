
import pandas as pd
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx",sheet_name="Export Worksheet")
df3 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
mergedf1 = pd.DataFrame(columns=['Subcat_ID','Stopwords'])
uniquesubcats = list(df2['SUBCAT_ID'].unique())
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
highfreqdict =df3.set_index('SUBCAT ID').T.to_dict('list')
a=0
i=0
row=0
while(a<len(df3)):
    if(df3.iloc[a]["SUBCAT ID"] in uniquesubcats and a<len(df3)):
        subcatid = df3.iloc[a]["SUBCAT ID"]
        j=i
        concatstring =""
        while(df2.iloc[i]["SUBCAT_ID"] == subcatid and i<=len(df2)-1):
            concatstring += df2.iloc[i]["GLCAT_MCAT_NAME"]+" "
            i=i+1
            if(i==len(df2)):
                break
        uniq = set(concatstring.split(' '))
        string1 =""
        for x in uniq:
            if x not in string1:
                string1+=x + " "
        mergedf1.set_value(row,'Subcat_ID',df2.iloc[j]["SUBCAT_ID"])
        s= string1 +" "+ str(highfreqdict[df2.iloc[j]["SUBCAT_ID"]][0])
        mergedf1.set_value(row,'Stopwords',s)
        row=row+1
        a=a+1
    elif(df3.iloc[a]["SUBCAT ID"] not in uniquesubcats and a<len(df3)):
        mergedf1.set_value(row,'Subcat_ID',df3.iloc[a]["SUBCAT ID"])
        mergedf1.set_value(row,'Stopwords',df3.iloc[a]["HIGH FREQUENCY WORDS"])
        row=row+1
        a=a+1
mergedf1.to_csv("700subcatwisefinalstopwords.csv",index=False)