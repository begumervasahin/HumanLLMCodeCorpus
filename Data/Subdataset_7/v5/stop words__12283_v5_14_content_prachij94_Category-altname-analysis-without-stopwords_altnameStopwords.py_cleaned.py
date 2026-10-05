import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_ALTMCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b4 = b3.set_index('SUBCAT ID')["HIGH FREQUENCY WORDS"].to_dict()
b5 = pd.DataFrame(columns=['MCAT_ID', 'MCAT_Name', 'Alt_Name', 'Subcat_ID', 'Stopword', 'Attribute'])
for _, group in b2.groupby("SUBCAT_ID"):
    b6 = group["SUBCAT_ID"].iloc[0]
    if b6 in b4:
        b7 = set(' '.join(group["GLCAT_MCAT_NAME"]).split())
        b8 = b4[b6]
        b5 = b5.append({
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': b6,
            'Stopword': b8,
            'Attribute': ' '.join(b7) + ' ' + b8
        }, b9 = True)
    else:
        b5 = b5.append({
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': b6,
            'Stopword': '',
            'Attribute': group["GLCAT_MCAT_NAME"].iloc[0]
        }, b9 = True)
for b13, row in b1.iterrows():
    b6 = row["FK_GLCAT_CAT_ID"]
    if b6 in b5["Subcat_ID"].values:
        b10 = b5.loc[b5["Subcat_ID"] == b6, "Stopword"].iloc[0]
        b11 = row["GLCAT_ALTMCAT_NAME"]
        b12 = ' '.join([word for word in b11.split() if word not in b10.split()])
    else:
        b10 = ''
        b12 = ''
    b5 = b5.append({
        'MCAT_ID': row["GLCAT_MCAT_ID"],
        'MCAT_Name': row["GLCAT_MCAT_NAME"],
        'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
        'Subcat_ID': b6,
        'Stopword': b10,
        'Attribute': b12.strip()
    }, b9 = True)
b5.to_csv("stopwordsremovedaltnames.csv", b13 = False)