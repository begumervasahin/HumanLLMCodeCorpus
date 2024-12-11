import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_ALTMCAT_NAME"] = b1["GLCAT_ALTMCAT_NAME"].str.lower()
b4 = b3.set_index('SUBCAT ID').T.to_dict('list')
b5 = b2.merge(b1, left_on='SUBCAT_ID', right_on='FK_GLCAT_CAT_ID', how='inner')
b5 = b5[['SUBCAT_ID', 'GLCAT_MCAT_NAME', 'GLCAT_ALTMCAT_NAME']].set_index('SUBCAT_ID').T.to_dict('list')
def fonk1(row):
    b6 = row['FK_GLCAT_CAT_ID']
    b7 = row['GLCAT_ALTMCAT_NAME']
    b8 = row['GLCAT_MCAT_NAME']
    if b6 in b5:
        b9 = b4[b6][0] if b6 in b4 else b5[b6][1]
        b10 = b7.split(" ")
        b11 = " ".join(word for word in b10 if word not in b9.split(" "))
        return b11.strip()
    else:
        return b7.strip()
b1['Attribute'] = b1.apply(process_alt_names, b12 = 1)
b1.to_csv("stopwordsremovedaltnames.csv", b13 = False)