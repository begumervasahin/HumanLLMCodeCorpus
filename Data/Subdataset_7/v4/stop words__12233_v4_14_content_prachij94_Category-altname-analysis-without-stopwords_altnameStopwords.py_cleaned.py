import pandas as pd
b1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
b2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
b3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
b3["HIGH FREQUENCY WORDS"] = b3["HIGH FREQUENCY WORDS"].str.lower()
b2["GLCAT_MCAT_NAME"] = b2["GLCAT_MCAT_NAME"].str.lower()
b1["GLCAT_ALTMCAT_NAME"] = b1["GLCAT_MCAT_NAME"].str.lower()
b4 = b3.set_index('SUBCAT ID')["HIGH FREQUENCY WORDS"].to_dict()
b5 = pd.DataFrame(columns=['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords'])
for _, group in b2.groupby("SUBCAT_ID"):
    b6 = group["SUBCAT_ID"].iloc[0]
    if b6 in b4:
        b7 = set(' '.join(group["GLCAT_MCAT_NAME"]).split())
        b8 = b4[b6]
        b9 = {
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': b6,
            'MCAT_Name&HighFrequencyWords': ' '.join(b7) + ' ' + b8
        }
    else:
        b9 = {
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': b6,
            'MCAT_Name&HighFrequencyWords': group["GLCAT_MCAT_NAME"].iloc[0]
        }
    b5 = b5.append(b9, ignore_index=True)
b10 = b5.set_index('Subcat_ID')["MCAT_Name&HighFrequencyWords"].to_dict()
b11 = ['MCAT_ID', 'MCAT_Name', 'Alt_Name', 'Subcat_ID', 'Stopword', 'Attribute']
b12 = pd.DataFrame(columns=b11)
for b16, row in b1.iterrows():
    b6 = row["FK_GLCAT_CAT_ID"]
    if b6 in b10:
        b13 = b10[b6]
        b14 = row["GLCAT_ALTMCAT_NAME"]
        b15 = ' '.join([word for word in b14.split() if word not in b13.split()])
        b9 = {
            'MCAT_ID': row["GLCAT_MCAT_ID"],
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
            'Subcat_ID': b6,
            'Stopword': b13,
            'Attribute': b15.strip()
        }
    else:
        b9 = {
            'MCAT_ID': row["GLCAT_MCAT_ID"],
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
            'Subcat_ID': b6,
            'Attribute': ''
        }
    b12 = b12.append(b9, ignore_index=True)
b12.to_csv("stopwordsremovedaltnames.csv", b16 = False)