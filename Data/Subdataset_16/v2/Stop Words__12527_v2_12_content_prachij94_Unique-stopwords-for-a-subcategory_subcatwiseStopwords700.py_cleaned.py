import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
b3 = pd.DataFrame(columns=['Subcat_ID', 'Stopwords'])
b4 = b1['SUBCAT_ID'].unique()
b2["HIGH FREQUENCY WORDS"] = b2["HIGH FREQUENCY WORDS"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b5 = b2.set_index('SUBCAT ID').T.to_dict('list')
a1 = 0
a2 = 0
a3 = 0
while a1 < len(b2):
    b6 = b2.iloc[a1]["SUBCAT ID"]
    if b6 in b4:
        b7 = ""
        while a2 < len(b1) and b1.iloc[a2]["SUBCAT_ID"] == b6:
            b7 += b1.iloc[a2]["GLCAT_MCAT_NAME"] + " "
            a2 += 1
        b8 = set(b7.split())
        b9 = " ".join(b8)
        b9 += " " + b5[b6][0]
        b3.loc[a3, 'Subcat_ID'] = b6
        b3.loc[a3, 'Stopwords'] = b9
    else:
        b3.loc[a3, 'Subcat_ID'] = b6
        b3.loc[a3, 'Stopwords'] = b2.iloc[a1]["HIGH FREQUENCY WORDS"]
    a3 += 1
    a1 += 1
b3.to_csv("700subcatwisefinalstopwords.csv", b10 = False)