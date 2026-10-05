import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_ALTMCAT_NAME"] = b1["GLCAT_ALTMCAT_NAME"].str.lower()
b4 = b3.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
b5 = b2.merge(b1, left_on='SUBCAT_ID', right_on='FK_GLCAT_CAT_ID', how='inner')
b5 = b5[['SUBCAT_ID', 'GLCAT_MCAT_NAME', 'GLCAT_ALTMCAT_NAME']].set_index('SUBCAT_ID').to_dict('b12')
def fonk1(row):
    b6 = row['FK_GLCAT_CAT_ID']
    b7 = row['GLCAT_ALTMCAT_NAME']
    if b6 in b5:
        b8 = b4.get(b6, b5[b6]['GLCAT_MCAT_NAME'])
        b9 = b7.split(" ")
        b10 = " ".join(word for word in b9 if word not in b8.split(" "))
        return b10.strip()
    else:
        return b7.strip()
b1['Attribute'] = b1.apply(process_alt_names, b11 = 1)
b1.to_csv("stopwordsremovedaltnames.csv", b12 = False)