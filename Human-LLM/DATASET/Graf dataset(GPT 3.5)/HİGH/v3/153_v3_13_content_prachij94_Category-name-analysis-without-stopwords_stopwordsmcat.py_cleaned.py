import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx", sheet_name="Sheet2")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_MCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b4 = b3.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
b5 = pd.DataFrame(columns=['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords'])
for b14, row in b2.iterrows():
    b6 = row["SUBCAT_ID"]
    if b6 in b4:
        b7 = row["GLCAT_MCAT_NAME"]
        b8 = set(b7.split())
        b8.difference_update(b4[b6].split())
        b9 = " ".join(b8)
        b5 = b5.append({
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Subcat_ID': b6,
            'MCAT_Name&HighFrequencyWords': b9 + " " + b4[b6]
        }, b10 = True)
    else:
        b5 = b5.append({
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Subcat_ID': b6,
            'MCAT_Name&HighFrequencyWords': row["GLCAT_MCAT_NAME"]
        }, b10 = True)
b11 = pd.DataFrame(columns=['MCAT_ID', 'PMCAT', 'MCAT_Name', 'Subcat_ID', 'Stopword', 'Attribute'])
for b14, row in b1.iterrows():
    b6 = row["FK_GLCAT_CAT_ID"]
    b12 = ""
    if b6 in b4:
        b13 = b4[b6]
    else:
        b13 = ""
    b7 = row["GLCAT_MCAT_NAME"]
    for word in b7.split():
        if word not in b13.split():
            b12 += " " + word
    b11 = b11.append({
        'MCAT_ID': row["GLCAT_MCAT_ID"],
        'PMCAT': row["PMCAT"],
        'MCAT_Name': row["GLCAT_MCAT_NAME"],
        'Subcat_ID': b6,
        'Stopword': b13,
        'Attribute': b12.strip()
    }, b10 = True)
b11['Attribute'] = b11['Attribute'].str.lstrip()
b11.to_csv("stopwordsremovedmcats.csv", b14 = False)