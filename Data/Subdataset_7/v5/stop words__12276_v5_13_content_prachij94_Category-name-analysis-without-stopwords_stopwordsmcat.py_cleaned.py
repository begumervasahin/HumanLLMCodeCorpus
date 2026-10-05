import pandas as pd
def fonk1(file_path, b1):
    return pd.fonk1(file_path, b1 = b1)
def fonk2(data_frame, column_name):
    if column_name in data_frame.columns:
        data_frame[column_name] = data_frame[column_name].str.lower()
b2 = fonk1("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx", "Sheet2")
b3 = fonk1("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", "Export Worksheet")
b4 = fonk1("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", "wordfrequencyfinal")
fonk2(b2, "GLCAT_MCAT_NAME")
fonk2(b3, "GLCAT_MCAT_NAME")
fonk2(b4, "HIGH FREQUENCY WORDS")
b5 = ['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords']
b6 = ['MCAT_ID', 'PMCAT', 'MCAT_Name', 'Subcat_ID', 'Stopword', 'Attribute']
b7 = pd.DataFrame(columns=b5)
b8 = pd.DataFrame(columns=b6)
b9 = b4.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
a1 = 0
for i in range(len(b3)):
    b10 = b3.at[i, "SUBCAT_ID"]
    if b10 in b9:
        b11 = i
        b12 = " ".join(set(b3.at[i, "GLCAT_MCAT_NAME"] for i in range(i, len(b3)) if b3.at[i, "SUBCAT_ID"] == b10))
        b13 = " ".join(set(b12.split(' ')))
        b7.loc[a1] = [b3.at[b11, "GLCAT_MCAT_NAME"], b10, f"{b13} {b9[b10]}"]
    else:
        b7.loc[a1] = [b3.at[i, "GLCAT_MCAT_NAME"], b10, b3.at[i, "GLCAT_MCAT_NAME"]]
    a1 += 1
b14 = b7.set_index('Subcat_ID')['MCAT_Name&HighFrequencyWords'].to_dict()
a1 = 0
for i in range(len(b2)):
    b10 = b2.at[i, "FK_GLCAT_CAT_ID"]
    if b10 in b14:
        b15 = b14[b10].split()[1]
    else:
        b15 = ""
    b16 = " ".join(word for word in b2.at[i, "GLCAT_MCAT_NAME"].split() if word not in b15.split())
    b8.loc[a1] = [b2.at[i, "GLCAT_MCAT_ID"], b2.at[i, "PMCAT"], b2.at[i, "GLCAT_MCAT_NAME"], b10, b15, b16]
    a1 += 1
b8['Attribute'] = b8['Attribute'].str.strip()
b8.to_csv("stopwordsremovedmcats.csv", b17 = False)