
import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
b3 = pd.DataFrame(columns=['Subcat_ID', 'Stopwords'])
b4 = b1['SUBCAT_ID'].unique()
b2["HIGH FREQUENCY WORDS"] = b2["HIGH FREQUENCY WORDS"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b5 = b2.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
a, i, b6 = 0, 0, 0
while a < len(b2):
    b7 = b2.iloc[a]["SUBCAT ID"]
    if b7 in b4:
        b8 = ""
        while i < len(b1) and b1.iloc[i]["SUBCAT_ID"] == b7:
            b8 += b1.iloc[i]["GLCAT_MCAT_NAME"] + " "
            i += 1
        b9 = set(b8.split())
        b10 = " ".join(b9) + " " + b5[b7]
        b3.loc[b6] = [b7, b10]
        b6 += 1
    else:
        b3.loc[b6] = [b7, b2.iloc[a]["HIGH FREQUENCY WORDS"]]
        b6 += 1
    a += 1
b3.to_csv("700subcatwisefinalstopwords.csv", b11 = False)