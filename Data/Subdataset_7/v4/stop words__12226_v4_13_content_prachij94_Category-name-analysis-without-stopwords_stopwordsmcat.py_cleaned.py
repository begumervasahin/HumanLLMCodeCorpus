import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx", sheet_name="Sheet2")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b4 = pd.DataFrame(columns=['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords'])
b5 = pd.DataFrame(columns=['MCAT_ID', 'PMCAT', 'MCAT_Name', 'Subcat_ID', 'Stopword', 'Attribute'])
b6 = b3.set_index('SUBCAT ID').T.to_dict('list')
a1 = 0
for i in range(len(b2)):
    b7 = b2.iloc[i]["SUBCAT_ID"]
    if b7 in b6.keys():
        b8 = i
        b9 = ""
        while i < len(b2) and b2.iloc[i]["SUBCAT_ID"] == b7:
            b9 += b2.iloc[i]["GLCAT_MCAT_NAME"] + " "
            i += 1
        b10 = set(b9.split(' '))
        b11 = " ".join(b10)
        b4.loc[a1, 'MCAT_Name'] = b2.iloc[b8]["GLCAT_MCAT_NAME"]
        b4.loc[a1, 'Subcat_ID'] = b2.iloc[b8]["SUBCAT_ID"]
        b4.loc[a1, 'MCAT_Name&HighFrequencyWords'] = b11 + " " + str(b6[b7][0])
        a1 += 1
    else:
        b4.loc[a1, 'MCAT_Name'] = b2.iloc[i]["GLCAT_MCAT_NAME"]
        b4.loc[a1, 'Subcat_ID'] = b2.iloc[i]["SUBCAT_ID"]
        b4.loc[a1, 'MCAT_Name&HighFrequencyWords'] = b2.iloc[i]["GLCAT_MCAT_NAME"]
        i += 1
        a1 += 1
b12 = b4[['Subcat_ID', 'MCAT_Name&HighFrequencyWords']].set_index('Subcat_ID').T.to_dict('list')
a1 = 0
for i in range(len(b1)):
    b7 = b1.iloc[i]["FK_GLCAT_CAT_ID"]
    if b7 in b12.keys():
        b13 = b12[b7][0]
    else:
        b13 = ""
    b14 = ""
    b15 = b1.iloc[i]["GLCAT_MCAT_NAME"]
    for x in b15.split(" "):
        if x not in b13.split(" "):
            b14 += " " + x
    b5.loc[a1, 'MCAT_ID'] = b1.iloc[i]["GLCAT_MCAT_ID"]
    b5.loc[a1, 'PMCAT'] = b1.iloc[i]["PMCAT"]
    b5.loc[a1, 'MCAT_Name'] = b1.iloc[i]["GLCAT_MCAT_NAME"]
    b5.loc[a1, 'Subcat_ID'] = b7
    b5.loc[a1, 'Stopword'] = b13
    b5.loc[a1, 'Attribute'] = b14.strip()
    a1 += 1
b5['Attribute'] = b5['Attribute'].str.lstrip()
b5.to_csv("stopwordsremovedmcats.csv", b16 = False)